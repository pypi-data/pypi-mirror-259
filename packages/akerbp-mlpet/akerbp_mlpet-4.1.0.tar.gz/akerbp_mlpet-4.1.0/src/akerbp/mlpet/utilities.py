import base64
import importlib.resources
import json
import os
import pickle
import re
import warnings
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable, Dict, List, Optional, Set, Tuple, Union, cast

import numpy as np
import numpy.typing as npt
import pandas as pd
from cognite.client import ClientConfig, CogniteClient
from cognite.client.credentials import OAuthClientCredentials
from cognite.client.data_classes import Asset, AssetList
from cryptography.hazmat.primitives import hashes, padding, serialization
from cryptography.hazmat.primitives.asymmetric import padding as asym_padding
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from numpy import float64
from scipy.interpolate import interp1d

import akerbp.mlpet.data
import akerbp.mlpet.preprocessors as preprocessors


def drop_rows_wo_label(df: pd.DataFrame, label_column: str, **kwargs) -> pd.DataFrame:
    """
    Removes columns with missing targets.

    Now that the imputation is done via pd.df.fillna(), what we need is the constant filler_value
    If the imputation is everdone using one of sklearn.impute methods or a similar API, we can use
    the indicator column (add_indicator=True)

    Args:
        df (pd.DataFrame): dataframe to process
        label_column (str): Name of the label column containing rows without labels

    Keyword Args:
        missing_label_value (str, optional): If nans are denoted differently than np.nans,
            a missing_label_value can be passed as a kwarg and all rows containing
            this missing_label_value in the label column will be dropped


    Returns:
        pd.DataFrame: processed dataframe
    """
    missing_label_value = kwargs.get("missing_label_value")
    if missing_label_value is not None:
        return df.loc[df[label_column] != missing_label_value, :]
    return df.loc[~df[label_column].isna(), :]


@lru_cache(maxsize=None)
def read_pickle(path):
    """
    A cached helper function for loading pickle files. Loading pickle files multiple
    times can really slow down execution

    Args:
        path (str): Path to the pickled object to be loaded

    Returns:
        data: Return the loaded pickled data
    """
    infile = Path(path).open("rb")
    data = pickle.load(infile, encoding="bytes")
    infile.close()
    return data


def map_formation_group_system(
    form_or_group_or_system: pd.Series, missing_value: Union[float, str] = np.nan
) -> Tuple[Union[float, str], Union[float, str], Union[float, str]]:
    """
    A helper function for retrieving the formation and group of a standardised
    formation/group based on mlpet's NPD pickle mapper.

    Args:
        form_or_group (pd.Series): A pandas series containing AkerBP legal
            formation/group names to be mapped
        MissingValue (Any): If no mapping is found, return this missing value

    Returns:
        tuple(pd.Series): Returns a formation and group series respectively corresponding
            to the input string series
    """
    with importlib.resources.path(
        akerbp.mlpet.data, "npd_fm_gp_sy_key_dic.pcl"
    ) as path:
        dic_names = read_pickle(path)

    mapping = {}
    for item in form_or_group_or_system.unique():
        form, group, siistem = missing_value, missing_value, missing_value
        try:
            dic = dic_names[item]
            name = dic["NAME"]
            parent = dic["PARENT"]
            grandparent = dic["GRANDPARENT"]
            if dic["LEVEL"] == "FORMATION":
                form = name
                group = parent
                siistem = grandparent
            elif dic["LEVEL"] == "GROUP":
                group = name
                siistem = grandparent
            elif dic["LEVEL"] == "SYSTEM":
                siistem = name
        except (KeyError, ValueError):
            pass
        form, group, siistem = pd.Series([form, group, siistem]).fillna(missing_value)
        mapping[item] = (form, group, siistem)

    form, group, siistem = zip(*form_or_group_or_system.map(mapping))  # type: ignore

    return form, group, siistem


def normalize_group_formation_system(
    df_: pd.DataFrame, add_systems=False
) -> pd.DataFrame:
    """
    A helper function to normalize a GROUP and FORMATION column using mlpet's
    builtin NPD mapper. A SYSTEM column can also optionally be added by setting
    add_systems to True.

    Args:
        add_systems (bool): Whether to add a SYSTEM column to the dataframe based
            on the GROUP and FORMATION columns mapping
        df_ (pd.DataFrame): The dataframe containing both the GROUP and FORMATION
            columns to be normalized

    Returns:
        pd.DataFrame: The dataframe with the normalization applied
    """
    if "FORMATION" in df_.columns:
        (
            df_["FORMATION"],
            df_["GROUP_MAPPED"],
            df_["SYSTEM_MAPPED_FM"],
        ) = map_formation_group_system(
            df_["FORMATION"].astype(str).apply(standardize_group_formation_name)
        )
    if "GROUP" in df_.columns:
        _, df_["GROUP"], df_["SYSTEM_MAPPED_GP"] = map_formation_group_system(
            df_["GROUP"].astype(str).apply(standardize_group_formation_name)
        )
        # NOTE: If GROUP is provided to this function and some filling is done,
        # ensure that the FORMATION column is adjusted as well. If a group is
        # inferred, a FORMATION should be set to UNKNOWN unless it was already
        # provided in the FORMATION column sent to this function

        # If formation is aviailable enrich the group column with it
        if "FORMATION" in df_.columns:
            # Special fix for increasing data quality of GROUP column
            fill_index = df_["FORMATION"].ne("UNKNOWN FM") & df_["GROUP"].eq(
                "UNKNOWN GP"
            )
            if fill_index.any():
                df_.loc[fill_index, "GROUP"] = df_.loc[fill_index, "GROUP_MAPPED"]

            # If no group information is available, use the formation mapped groups
            df_["GROUP"] = df_["GROUP"].fillna(df_["GROUP_MAPPED"])
    if add_systems:
        if "SYSTEM" in df_.columns:
            _, _, df_["SYSTEM"] = map_formation_group_system(
                df_["SYSTEM"].astype(str).apply(standardize_group_formation_name)
            )
        else:
            df_["SYSTEM"] = np.nan
        for col in ["SYSTEM_MAPPED_GP", "SYSTEM_MAPPED_FM"]:
            if col in df_.columns:
                df_["SYSTEM"] = df_["SYSTEM"].fillna(df_[col])

    df_ = df_.drop(
        columns=["GROUP_MAPPED", "SYSTEM_MAPPED_FM", "SYSTEM_MAPPED_GP"],
        errors="ignore",
    )

    return df_


def standardize_group_formation_name(name: Union[str, Any]) -> Union[str, Any]:
    """
    Performs several string operations to standardize group formation names
    for later categorisation.

    Args:
        name (str): A group formation name

    Returns:
        float or str: Returns the standardized group formation name or np.nan
            if the name == "NAN".
    """

    def __split(string: str) -> str:
        string = string.split(" ")[0]
        string = string.split("_")[0]
        return string

    def __format(string: str) -> str:
        string = string.replace("AA", "A")
        string = string.replace("Å", "A")
        string = string.replace("AE", "A")
        string = string.replace("Æ", "A")
        string = string.replace("OE", "O")
        string = string.replace("Ø", "O")
        return string

    # First perform some formatting to ensure consistencies in the checks
    name = str(name).upper().strip()
    # Replace NAN string with actual nan
    if name == "NAN":
        return np.nan
    # GPs & FMs with no definition leave as is
    unknown = [
        "NO FORMAL NAME",
        "NO GROUP DEFINED",
        "UNDEFINED",
        "UNDIFFERENTIATED",
        "UNKNOWN",
    ]
    for item in unknown:
        if item in name.upper():
            return "UNKNOWN"

    # Remove known prefixes
    known_prefixes = ["LOWER", "MIDDLE", "UPPER", "INTRA"]
    for prefix in known_prefixes:
        if prefix == "INTRA" and "FM" in name:
            name = re.sub("FM.*", "FM", name)
        name = name.replace(prefix, "").strip()

    # Then perform standardization
    if "(" in name and ")" in name:
        # Remove text between parantheses including the parentheses
        name = re.sub(r"[\(].*?[\)]", "", name).strip()
        name = __split(name)
    elif name == "TD":
        name = "TOTAL DEPTH"
    else:
        name = __split(name)

    # Format
    name = __format(name)

    return name


def standardize_names(
    names: List[str], mapper: Dict[str, str]
) -> Tuple[List[str], Dict[str, str]]:
    """
    Standardize curve names in a list based on the curve_mappings dictionary.
    Any columns not in the dictionary are ignored.

    Args:
        names (list): list with curves names
        mapper (dictionary): dictionary with mappings. Defaults to curve_mappings.

    Returns:
        list: list of strings with standardized curve names
    """
    standardized_names = []
    for name in names:
        mapped_name = mapper.get(name)
        if mapped_name:
            standardized_names.append(mapped_name)
        else:
            standardized_names.append(name)
    old_new_cols = {n: o for o, n in zip(names, standardized_names)}
    return standardized_names, old_new_cols


def standardize_curve_names(df: pd.DataFrame, mapper: Dict[str, str]) -> pd.DataFrame:
    """
    Standardize curve names in a dataframe based on the curve_mappings dictionary.
    Any columns not in the dictionary are ignored.

    Args:
        df (pd.DataFrame): dataframe to which apply standardization of columns names
        mapper (dictionary): dictionary with mappings. Defaults to curve_mappings.
            They keys should be the old curve name and the values the desired
            curved name.

    Returns:
        pd.DataFrame: dataframe with columns names standardized
    """
    return df.rename(columns=mapper)


def get_col_types(
    df: pd.DataFrame, categorical_curves: Optional[List[str]] = None, warn: bool = True
) -> Tuple[List[str], List[str]]:
    """
    Returns lists of numerical and categorical columns

    Args:
        df (pd.DataFrame): dataframe with columns to classify
        categorical_curves (list): List of column names that should be considered as
            categorical. Defaults to an empty list.
        warn (bool): Whether to warn the user if categorical curves were
            detected which were not in the provided categorical curves list.

    Returns:
        tuple: lists of numerical and categorical columns
    """
    if categorical_curves is None:
        categorical_curves = []
    cat_original: Set[str] = set(categorical_curves)
    # Make sure we are comparing apples with apples. Sometimes cat_original
    # will contain column names that are no longer in the passed df and this
    # will cause a false positive and trigger the first if check below. So
    # ensure that all cols in cat_original are in the df before proceeding.
    cat_original = {c for c in cat_original if c in df.columns}
    num_cols = set(df.select_dtypes(include="number").columns)
    cat_cols = set(df.columns) - num_cols
    if warn:
        if cat_cols != cat_original:
            extra = cat_original - cat_cols
            if extra:
                warnings.warn(
                    f"Cols {extra} were specified as categorical by user even though"
                    " they are numerical. Note: These column names are the names"
                    " after they have been mapped using the provided mappings.yaml!"
                    " So it could be another column from your original data that"
                    " triggered this warning and instead was mapped to one of the"
                    " names printed above.",
                    stacklevel=2,
                )
            extra = cat_cols - cat_original
            if extra:
                warnings.warn(
                    f"Cols {extra} were identified as categorical and are being"
                    " treated as such. Note: These column names"
                    " are the names after they have been mapped using the provided"
                    " mappings.yaml! So it could be another column from your"
                    " original data that triggered this warning and instead was"
                    " mapped to one of the names printed above.",
                    stacklevel=2,
                )
    cat_cols = cat_original.union(cat_cols)
    # make sure nothing from categorical is in num cols
    num_cols = num_cols - cat_cols
    return list(num_cols), list(cat_cols)


def wells_split_train_test(
    df: pd.DataFrame, id_column: str, test_size: float, **kwargs
) -> Tuple[List[str], List[str], List[str]]:
    """
    Splits wells into two groups (train and val/test)

    NOTE: Set operations are used to perform the splits so ordering is not
        preserved! The well IDs will be randomly ordered.

    Args:
        df (pd.DataFrame): dataframe with data of wells and well ID
        id_column (str): The name of the column containing well names which will
            be used to perform the split.
        test_size (float): percentage (0-1) of wells to be in val/test data

    Returns:
        wells (list): well IDs
        test_wells (list): wells IDs of val/test data
        training_wells (list): wells IDs of training data
    """
    wells = set(df[id_column].unique())
    rng: np.random.Generator = np.random.default_rng()
    test_wells = set(rng.choice(list(wells), int(len(wells) * test_size)))
    training_wells = wells - test_wells
    return list(wells), list(test_wells), list(training_wells)


def df_split_train_test(
    df: pd.DataFrame,
    id_column: str,
    test_size: float = 0.2,
    test_wells: Optional[List[str]] = None,
    **kwargs,
) -> Tuple[pd.DataFrame, pd.DataFrame, List[str]]:
    """
    Splits dataframe into two groups: train and val/test set.

    Args:
        df (pd.Dataframe): dataframe to split
        id_column (str): The name of the column containing well names which will
            be used to perform the split.
        test_size (float, optional): size of val/test data. Defaults to 0.2.
        test_wells (list, optional): list of wells to be in val/test data. Defaults to None.

    Returns:
        tuple: dataframes for train and test sets, and list of test well IDs
    """
    if test_wells is None:
        test_wells = wells_split_train_test(df, id_column, test_size, **kwargs)[1]
        if not test_wells:
            raise ValueError(
                "Not enough wells in your dataset to perform the requested train "
                "test split!"
            )
    df_test = df.loc[df[id_column].isin(test_wells)]
    df_train = df.loc[~df[id_column].isin(test_wells)]
    return df_train, df_test, test_wells


def train_test_split(
    df: pd.DataFrame, target_column: str, id_column: str, **kwargs
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Splits a dataset into training and val/test sets by well (i.e. for an
    80-20 split, the provided dataset would need data from at least 5 wells).

    This function makes use of several other utility functions. The workflow it
    executes is:

        1. Drops row without labels
        2. Splits into train and test sets using df_split_train_test which in
            turn performs the split via wells_split_train_test

    Args:
        df (pd.DataFrame, optional): dataframe with data
        target_column (str): Name of the target column (y)
        id_column (str): Name of the wells ID column. This is used to perform
            the split based on well ID.

    Keyword Args:
        test_size (float, optional): size of val/test data. Defaults to 0.2.
        test_wells (list, optional): list of wells to be in val/test data. Defaults to None.
        missing_label_value (str, optional): If nans are denoted differently than np.nans,
            a missing_label_value can be passed as a kwarg and all rows containing
            this missing_label_value in the label column will be dropped

    Returns:
        tuple: dataframes for train and test sets, and list of test wells IDs
    """
    df = drop_rows_wo_label(df, target_column, **kwargs)
    df_train, df_test, _ = df_split_train_test(df, id_column, **kwargs)
    return df_train, df_test


def feature_target_split(
    df: pd.DataFrame, target_column: str
) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """
    Splits set into features and target

    Args:
        df (pd.DataFrame): dataframe to be split
        target_column (str): target column name

    Returns:
        tuple: input (features) and output (target) dataframes
    """
    X = df.loc[:, ~df.columns.isin([target_column])]  # noqa: N806
    y = df[target_column]
    return X, y


def normalize(
    col: pd.Series, ref_min: float64, ref_max: float64, col_min: float, col_max: float
) -> pd.Series:
    """
    Helper function that applies min-max normalization on a pandas series and
    rescales it according to a reference range according to the following formula:

        ref_low + ((col - col_min) * (ref_max - ref_min) / (col_max - col_min))

    Args:
        col (pd.Series): column from dataframe to normalize (series)
        ref_low (float): min value of the column of the well of reference
        ref_high (float): max value of the column of the well of reference
        well_low (float): min value of the column of well to normalize
        well_high (float): max value of the column of well to normalize

    Returns:
        pd.Series: normalized series
    """
    diff_ref = ref_max - ref_min
    diff_well = col_max - col_min
    with np.errstate(divide="ignore", invalid="ignore"):
        norm = ref_min + diff_ref * (col - col_min) / diff_well
    return norm


# Specifically ignoring complexity for this function because it would not
# make sense to split out the sub components into the utilities module
def get_well_metadata(  # noqa: C901
    client: CogniteClient, well_names: List[str]
) -> Dict[str, Dict[str, Any]]:
    """
    Retrieve relevant well metadata for the provided well_names

    Warning:
        If a well is not found in the asset database, it is not returned
        in the returned dictionary. Instead a warning is printed to the console
        with the corresponding well name.

    Metadata retrieved:

        - COMPLETION_DATE
        - COORD_SYSTEM_NAME
        - KB_ELEV
        - KB_ELEV_OUOM
        - PUBLIC
        - SPUD_DATE
        - WATER_DEPTH
        - CDF_wellName
        - WATER_DEPTH_DSDSUNIT
        - X_COORDINATE
        - Y_COORDINATE
        - DATUM_ELEVATION
        - DATUM_ELEVATION_UNIT
        - LATITUDE
        - LONGITUDE

    Args:
        client (CogniteClient): A connected cognite client instance
        well_names (List): The list of well names to retrieve metadata for

    Returns:
        dict: Returns a dictionary where the keys are the well names and the
            values are dictionaries with metadata keys and values.

    Example:
        Example return dictionary::

            {
                '25/10-10': {
                    'COMPLETION_DATE': '2010-04-02T00:00:00',
                    'COORD_SYSTEM_NAME': 'ED50 / UTM zone 31N',
                    'DATUM_ELEVATION': '0.0',
                    ...},
                '25/10-12 ST2': {
                    'COMPLETION_DATE': '2015-01-18T00:00:00',
                    'COORD_SYSTEM_NAME': 'ED50 / UTM zone 31N',
                    'DATUM_ELEVATION': nan,
                    ...},
            }
    """
    relevant_metadata_keys = [
        "WATER_DEPTH",
        "WATER_DEPTH_DSDSUNIT",
        "KB_ELEV",
        "KB_ELEV_OUOM",
        "PUBLIC",
        "Latitude",
        "Longitude",
        "SURFACE_NODE_LATITUDE",
        "SURFACE_NODE_LONGITUDE",
        "COORD_SYSTEM_NAME",
        "X_COORD",
        "X_COORDINATE",
        "Y_COORD",
        "Y_COORDINATE",
        "loc-x",
        "loc-y",
        "loc-x",
        "y-loc",
        "x",
        "y",
        "DATUM_ELEVATION",
        "DATUM_ELEVATION_DSDSUNIT",
        "DATUM_TYPE",
        "datum-elevation",
        "datum-unit",
        "SPUD_DATE",
        "COMPLETION_DATE",
        "WELLBORE_LOCATION_SPATIAL",
    ]

    # The order in which the similar keys are defined will determine which
    # key to chose if there are multiple unique values for similar keys!
    map_similar_keys = {
        "X_COORDINATE": [
            "X_COORDINATE",
            "X_COORD",
            "loc-x",
            "x-loc",
        ],
        "Y_COORDINATE": [
            "Y_COORDINATE",
            "Y_COORD",
            "loc-y",
            "y-loc",
        ],
        "DATUM_ELEVATION": [
            "DATUM_ELEVATION",
            "datum-elevation",
        ],
        "DATUM_ELEVATION_UNIT": [
            "DATUM_ELEVATION_DSDS_UNIT",
            "datum-unit",
        ],
        "LATITUDE": [
            "Latitude",
            "SURFACE_NODE_LATITUDE",
        ],
        "LONGITUDE": [
            "Longitude",
            "SURFACE_NODE_LONGITUDE",
        ],
    }

    # Helper function to find best match from fuzzy search results
    def _find_best_match(
        assetlist: AssetList, well_name: str
    ) -> Tuple[str, Optional[Asset]]:
        # Compares only the alphanumerics of the wellName (ie. punctuation removed)
        # If no match is found it returns an empty string
        pat = re.compile(r"[^a-zA-Z0-9]+")

        def _stripper(s: str, split: str) -> str:
            return pat.sub("", s).rsplit(split)[0].strip()

        for asset in assetlist:
            name = cast(str, asset.name)
            if _stripper(name, "T") == _stripper(well_name, "T"):
                return name, asset
            elif _stripper(name, "R") == _stripper(well_name, "R"):
                return name, asset
        return "", None

    # Helper function to retrieve asset with most relevant metadata in the case
    # of multiple matches
    def _merge_assets(assetlist: List[Optional[Asset]]) -> pd.Series:
        metadata = {}
        for asset in assetlist:
            if asset is not None:
                metadata.update(asset.to_pandas().squeeze().to_dict())

        merged = pd.Series(metadata, name=metadata["name"])
        return merged

    # First retrieve metadata from the Cognite asset API
    meta = []
    for well in well_names:
        try:
            # First try list search
            assets: Union[AssetList, List[Optional[Asset]]] = client.assets.list(
                name=well,
                metadata={"type": "Wellbore"},
            )
            if len(assets) == 0:
                # If first attempt failed try a list search again but assuming
                # the well name was specified in techlog form
                tl_well_name = well.replace("_", "/", 1).replace("_", " ")
                assets = client.assets.list(
                    name=tl_well_name,
                    metadata={"type": "Wellbore"},
                )
                if len(assets) == 0:
                    # If second attempt fails use fuzzy search to retrieve proper
                    # well name. Find best match based on alphanumeric equality
                    well_name, asset = _find_best_match(
                        client.assets.search(
                            name=well,
                            filter={"metadata": {"type": "Wellbore"}},
                            limit=10,
                        ),
                        well,
                    )
                    if not well_name:
                        raise IndexError
                    assets = [asset]
                else:
                    well_name = tl_well_name
                warnings.warn(
                    f"Could not find a direct match for '{well}' in the CDF Assets"
                    f" database. Closest match found is '{well_name}'. Using the "
                    "metadata from that asset!",
                    stacklevel=2,
                )
            if len(assets) > 1:
                # Sort by time with first element being most recent
                assets = sorted(assets, key=lambda x: x.last_updated_time)
                # Some wells are stored several times as assets??
                # In this case merge them all together to retrieve as much
                # metadata as possible.
                series_meta = _merge_assets(assets)
            else:
                asset = assets[0]
                if asset is None:
                    raise IndexError
                series_meta = asset.to_pandas().squeeze()
                series_meta.name = asset.name
        except IndexError:
            # No match found for the well in the asset database.
            warnings.warn(
                f"Could not find any metadata for well: {well}",
                stacklevel=2,
            )
            continue

        # Filter retrieved series to only relevant keys and save CDF well name
        series_meta = series_meta.loc[
            series_meta.index.intersection(relevant_metadata_keys)
        ].copy()
        series_meta.loc["CDF_wellName"] = series_meta.name
        series_meta.name = well

        meta.append(series_meta)

    cdf_meta = pd.concat(meta, axis=1)

    # Need to handle WELLBORE_LOCATION_SPATIAL specially
    if "WELLBORE_LOCATION_SPATIAL" in cdf_meta.index:
        sub = (
            cdf_meta.loc["WELLBORE_LOCATION_SPATIAL"]
            .replace("null", np.nan)
            .dropna()
            .apply(eval)
            .copy()
        )
        restructured = pd.json_normalize(sub)[["x", "y"]]
        restructured.index = sub.index
        restructured = restructured.explode("x").explode("y").T
        cdf_meta = pd.concat([cdf_meta, restructured], axis=0)
        cdf_meta = cdf_meta.loc[~cdf_meta.index.isin(["WELLBORE_LOCATION_SPATIAL"])]

    # Then group mapped keys
    # Helper function for apply operation
    def _apply_function(x: pd.Series, highest_rank_key: List[str]) -> Any:
        unique = x.dropna().unique()
        # Check for multiple unique values per well (float & string)
        if len(unique) > 1:
            # Return the key off highest rank
            return x.loc[highest_rank_key]
        elif len(unique) == 0:
            return np.nan
        else:
            return unique[0]

    for mapping_name, mapping in map_similar_keys.items():
        # filter to relevant mapping
        idx = cdf_meta.index.intersection(mapping)
        if len(idx) == 0:  # No metadata matching this mapping
            continue
        elif len(idx) == 1:  # One key matching this mapping so just use it's values
            values = cdf_meta.loc[idx].squeeze()
        else:
            # Respect order of similar key mapping
            highest_rank_key = idx[np.argmin([mapping.index(x) for x in idx])]
            values = cdf_meta.loc[idx].apply(
                lambda x: _apply_function(x, highest_rank_key),  # noqa: B023
                axis=0,  # noqa: B023
            )
            values.name = mapping_name
        cdf_meta = cdf_meta.loc[~cdf_meta.index.isin(idx)]
        cdf_meta.loc[mapping_name] = values

    metadata_dict: Dict[str, Dict[str, Any]] = cdf_meta.to_dict()
    return metadata_dict


def get_formation_tops(  # noqa: C901
    well_names: List[str],
    client: CogniteClient,
    data_source: str = "NPD",
    **kwargs,
) -> Dict[str, Dict[str, Any]]:
    """
    Retrieves formation tops metadata for a provided list of well names (IDs) from
    CDF and returns them in a dictionary of depth levels and labels per well.

    Args:
        well_names (str): A list of well names (IDs)
        client (CogniteClient): A connected instance of the Cognite Client.

    Keyword Args:
        undefined_name (str): Name for undefined formation/group tops.
            Defaults to 'UNKNOWN'
        load_from_gis (bool): Indicator for whether try to fetch formation tops from GIS if not found in CDF.
            This option require access for user and might give errormessage.
            Defaults to False
        data_source (str): The data source to use for formation tops when retrieving from CDF. Can be either 'NPD' or 'Studio'.

    NOTE: The formation will be skipped if it's only 1m thick.
            NPD do not provide technial side tracks,
            such that information (formation tops) provided
            by NPD is missing T-labels.

    Returns:
        Dict: Returns a dictionary of formation tops metadata per map in this
            format::

                formation_tops_mapper = {
                    "31/6-6": {
                        "group_labels": ['Nordland Group', 'Hordaland Group', ...],
                        "group_labels_chronostrat": ['Cenozoic', 'Paleogene', ...]
                        "group_levels": [336.0, 531.0, 650.0, ...],
                        "formation_labels": ['Balder Formation', 'Sele Formation', ...],
                        "formation_labels_chronostrat": ['Eocene', 'Paleocene', ...],
                        "formation_levels": [650.0, 798.0, 949.0, ...]
                    }
                    ...
                }
    NOTE: The length of the levels entries equals the length of the corresponding labels entries + 1,
            such that the first entry of a label entry lies between the first and the second entries
            of the corresponding level entry.
    """
    undefined_name: str = kwargs.get("undefined_name", "UNKNOWN")
    load_from_gis: str = kwargs.get("load_from_gis", False)

    formation_tops_mapper = {}
    for well in well_names:
        well_name = well.split("T")[0].strip()

        tops = client.sequences.list(
            metadata={
                "wellbore_name": well_name,
                "type": "FormationTops",
                "source": data_source,
            }
        )
        if tops is None or len(tops) == 0:
            if load_from_gis:
                try:
                    try:
                        import pyodbc
                    except ImportError as e:
                        raise Exception(
                            "Could not import pyodbc. If you are on a Unix "
                            "system, you need to install additional libraries "
                            "to be able to use pyodbc. See "
                            "https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=ubuntu18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline"
                        ) from e

                    try:
                        cnxn = pyodbc.connect(
                            "DRIVER={SQL Server};SERVER=arcgis2.db.pertra.locale\\felles;DATABASE=GISData;Trusted_Connection=yes;"
                        )
                    except pyodbc.Error as e:
                        raise Exception(
                            "Could not connect to GIS database. Please make sure you are connected to the Aker BP network."
                        ) from e
                    sql_query = f"SELECT Wellbore, Chronostrat, Lithostrat, Top_MD, Base_MD FROM gisdata.Well_tops WHERE Wellbore='{well_name}'"
                    rows = pd.read_sql(sql_query, cnxn).sort_values([
                        "Top_MD",
                        "Base_MD",
                    ])

                    for i, r in rows.iterrows():
                        rows.loc[i, "Lithostrat"] = standardize_group_formation_name(
                            r.Lithostrat
                        )
                    rows["FORMATION"], rows["GROUP"], _ = map_formation_group_system(
                        form_or_group_or_system=rows.Lithostrat, missing_value="UNKNOWN"
                    )

                    # For formation without a group recording to mapping
                    # Assume group is similar to level above
                    # Do not assume anything for the formation
                    for i, r in rows.iterrows():
                        if r["GROUP"] == "UNKNOWN":
                            rows.loc[i, "GROUP"] = rows.loc[i - 1, "GROUP"]

                    rows_groups = rows.sort_values(["Top_MD", "Base_MD"]).copy()
                    rows_groups["Level"] = "GROUP"
                    rows_groups["Lithostrat"] = rows_groups["GROUP"]

                    rows_formations = rows.sort_values(["Top_MD", "Base_MD"]).copy()
                    rows_formations["Level"] = "FORMATION"
                    rows_formations["Lithostrat"] = rows_formations["FORMATION"]
                except Exception:
                    warnings.warn(
                        f"No formation tops information was found for {well} in CDF or GIS. Skipping it!",
                        stacklevel=2,
                    )
                    continue
            else:
                warnings.warn(
                    f"No formation tops information was found for {well} in CDF. Skipping it!",
                    stacklevel=2,
                )
                continue
        else:
            rows = tops[0].rows(start=0, end=None).to_pandas()

            rows_groups = rows[rows.Level == "GROUP"].sort_values(["Top_MD", "Base_MD"])
            rows_formations = rows[rows.Level == "FORMATION"].sort_values([
                "Top_MD",
                "Base_MD",
            ])

        group_labels: List[str] = []
        chrono_group_labels: List[str] = []
        group_levels: List[float] = []
        formation_labels: List[str] = []
        chrono_formation_labels: List[str] = []
        formation_levels: List[float] = []
        label = undefined_name

        # Groups ###
        for _, row in rows_groups.iterrows():
            # Skip group is length is 1m
            if row.Top_MD == row.Base_MD:
                continue
            new_label = row.Lithostrat
            new_chrono_label = row.Chronostrat

            # If we have an undefined zone, merge it with the zone above to ensure
            # we don't reset groupwise trends and try to preserve continuity.
            # We choose "undefined" here because this applies to a select few
            # edge cases
            if label == new_label or new_label.lower().startswith(
                "undefined"
            ):  # merge levels
                group_levels = group_levels[:-1]
                group_levels.append(row.Base_MD)
            else:
                try:
                    if row.Top_MD != group_levels[-1]:  # groups not continuous
                        group_labels.append(undefined_name)
                        chrono_group_labels.append(undefined_name)
                        group_levels.extend([group_levels[-1], row.Top_MD])
                except Exception:
                    pass
                label = new_label
                chrono_label = new_chrono_label
                group_labels.append(label)
                chrono_group_labels.append(chrono_label)
                group_levels.extend([row.Top_MD, row.Base_MD])
        group_levels = list(dict.fromkeys(group_levels))
        assert len(chrono_group_labels) == len(
            group_labels
        ), "Chronostrat labels no consistent with groups"

        # Formations ###
        label = undefined_name
        for _, row in rows_formations.iterrows():
            # Skip formation is length is 1m
            if row.Top_MD == row.Base_MD:
                continue
            new_label = row.Lithostrat
            new_chrono_label = row.Chronostrat
            if label == new_label or new_label.lower().startswith("undefined"):
                formation_levels = formation_levels[:-1]
                formation_levels.append(row.Base_MD)
            else:
                try:
                    if row.Top_MD != formation_levels[-1]:  # groups not continuous
                        formation_labels.append(undefined_name)
                        chrono_formation_labels.append(undefined_name)
                        formation_levels.extend([formation_levels[-1], row.Top_MD])
                except Exception:
                    pass
                label = new_label
                chrono_label = new_chrono_label
                formation_labels.append(label)
                chrono_formation_labels.append(chrono_label)
                formation_levels.extend([row.Top_MD, row.Base_MD])
        formation_levels = list(dict.fromkeys(formation_levels))
        assert len(chrono_formation_labels) == len(
            formation_labels
        ), "Chronostrat labels no consistent with formations"

        formation_tops_mapper[well] = {
            "group_labels": group_labels,
            "group_labels_chronostrat": chrono_group_labels,
            "group_levels": group_levels,
            "formation_labels": formation_labels,
            "formation_labels_chronostrat": chrono_formation_labels,
            "formation_levels": formation_levels,
        }
    return formation_tops_mapper


def get_trajectory_mapper_from_cdf(
    well_names: List[str],
    client: CogniteClient,
) -> Dict[str, Dict[str, List[float]]]:
    """Makes a query to CDF for all provided wells and extracts trajectory data, i.e.
    vertical- and measured depths as well as coordinates.

    The resulting dictionary have keys representing each well being queried, with values being
    a mapping dictionary with the following keys
        - MD
        - TVDKB
        - TVDSS
        - TVDBML
        - X
        - Y

    Note that the resulting values are not for the entire wellbore, so these needs to be interpolated
    using measured depth (MD) as a reference.

    Args:
        well_name (List[str]): list of well names
        client (CogniteClient): cognite client

    Returns:
        Dict[str, Dict[str, List[float]]]: Dictionary containing trajectory data (values) for each well (keys)
    """
    trajectory_mapper = {}
    for well in well_names:
        # Trajectory in CDF is fetched from GIS, which agian is fetched from NPD.
        # NPD do not keep track of technical sidetrackings.
        well_name = well.split("T")[0].rstrip()
        well_data_cdf = client.sequences.list(
            metadata={"wellbore_name": well_name, "type": "trajectory"},
            limit=None,
        )
        if len(well_data_cdf) == 0:
            warnings.warn(
                f"No trajectory data was found for well {well}. Skipping it!",
                stacklevel=2,
            )
            continue
        well_df_discrete = client.sequences.data.retrieve_dataframe(
            id=well_data_cdf[0].id,
            start=0,
            end=None,
        )
        if len(well_df_discrete) == 0:
            warnings.warn(
                f"No trajectory data was found for well {well}. Skipping it!",
                stacklevel=2,
            )
            continue
        well_df_discrete = well_df_discrete.drop_duplicates(subset=["MD"]).sort_values(
            by=["MD"]
        )
        well_df_discrete["TVDSS"] = -well_df_discrete["TVDSS"]
        trajectory_mapper_well = well_df_discrete[
            ["MD", "TVDKB", "TVDSS", "TVDBML", "X", "Y"]
        ].to_dict(orient="list")
        trajectory_mapper[well] = trajectory_mapper_well

    return trajectory_mapper


def drop_fields_from_trajectory_mapper(
    trajectory_mapper: Dict[str, Dict[str, List[float]]], fields_to_drop: List[str]
) -> Dict[str, Dict[str, List[float]]]:
    """Drop specified fields from the trajectory mapping dictionary from CDF

    Args:
        trajectory_mapper (Dict[str, List[float]]): trajectory mapping dictionary
        fields_to_drop (List[str]): fields to exclude from the mapping dictionary

    Returns:
        Dict[str, Dict[str, List[float]]]: trajectory mapping dictionary
    """
    mapper = {}
    for well, trajectory_dict in trajectory_mapper.items():
        for field in fields_to_drop:
            try:
                trajectory_dict.pop(field)
            except KeyError:
                warnings.warn(
                    f"Specified field '{field}' does not exist in the trajectory mapping and can not be removed",
                    stacklevel=2,
                )
                continue
        mapper[well] = trajectory_dict
    return mapper


def get_wellbore_coordinates(
    well_names: List[str],
    client: CogniteClient,
) -> Dict[str, Dict[str, List[float]]]:
    """Returns a dictionary with well names as keys, and a dictionary with
    X and Y coordinates as well as measured depth (MD) as values.

    These are values at discrete points along the wellbore.

    Args:
        well_names (List[str]): List of well names
        client (CogniteClient): CogniteClient object

    Returns:
        Dict[str, Dict[str, List[float]]]: Dictionary with well names as keys,
        and a dictionary with x, y, and z values as values.
    """
    fields_to_drop = ["TVDKB", "TVDSS", "TVDBML"]
    trajectory_mapper = get_trajectory_mapper_from_cdf(well_names, client)
    coordinates_mapper = drop_fields_from_trajectory_mapper(
        trajectory_mapper, fields_to_drop
    )
    return coordinates_mapper


def get_vertical_depths(
    well_names: List[str],
    client: CogniteClient,
) -> Dict[str, Dict[str, List[float]]]:
    """Returns a dictionary with well names as keys, and a dictionary with
    vertical- and measured depths as values.

    These are values at discrete points along the wellbore.

    Args:
        well_names (List[str]): list of well names
        client (CogniteClient): cognite client

    Returns:
        Dict[str, Dict[str, List[float]]]: Dictionary containing vertical- and measured depths (values) for each well (keys), list of wells with empty trajectory query to CDF
    """
    fields_to_drop = ["X", "Y"]
    trajectory_mapper = get_trajectory_mapper_from_cdf(well_names, client)
    vertical_depths_mapper = drop_fields_from_trajectory_mapper(
        trajectory_mapper, fields_to_drop
    )

    return vertical_depths_mapper


def interpolate_discrete_trajectory_data_along_wellbore(
    df: pd.DataFrame,
    id_column: str,
    md_column: str,
    trajectory_mapping: Dict[str, Dict[str, List[float]]],
) -> pd.DataFrame:
    """Linearly interpolate the discrete trajectory data along the entire wellbore

    Args:
        df (pd.DataFrame): input data
        id_column (str): column representing well name
        md_column (str): column representing measured depth
        trajectory_mapping (Dict[str, Dict[str, List[float]]]): trajectory mapping

    Returns:
        pd.DataFrame: output data with interpolated trajectory data as additinoal colmns
    """
    df_ = df.copy()
    for well in trajectory_mapping:
        md_interpolate = df_.loc[df_[id_column] == well, md_column].to_list()
        trajectory_data = trajectory_mapping[well]
        md = trajectory_data["MD"]
        for trajectory_field in trajectory_data.keys():
            if trajectory_field == "MD":
                continue
            trajectory_values = trajectory_data[trajectory_field]
            with warnings.catch_warnings(record=True) as w:
                f = interp1d(x=md, y=trajectory_values, fill_value="extrapolate")
                interpolated_trajectory_values = f(md_interpolate)
            if w:
                warnings.warn(
                    f"Interpolation of {trajectory_field} for well {well} triggered a "
                    f"runtime warning: {w[0].message}",
                    stacklevel=2,
                )
            df_.loc[df_[id_column] == well, trajectory_field] = (
                interpolated_trajectory_values
            )
    return df_


def get_calibration_map(
    df: pd.DataFrame,
    curves: List[str],
    location_curves: List[str],
    mode: str,
    id_column: str,
    levels: Optional[List[str]] = None,
    standardize_level_names: bool = True,
) -> Dict[str, pd.DataFrame]:
    """
    Returns calibration maps for each level, per well, typically formation and group.
    Calibration maps are pandas dataframes with the well name and unique values for
    each curve and location, where the value is the chosen "mode", such as mean,
    median, mode, etc, specified by the user. Useful for functions
    preprocessors.apply_calibration() and imputers.fillna_callibration_values().

    Args:
        df (pd.DataFrame): dataframe with wells data
        curves (List[str]): list of curves to fetch unique values
        location_curves (List[str]): list of curves indicating location of
        well/formation/group.
        Typically latitude, longitude, tvdbml, depth
        mode (str): any method supported in pandas dataframe for representing the curve,
        such as median, mean, mode, min, max, etc.
        id_column (str): column with well names
        levels (List[str], optional): how to group samples in a well, typically per
        group or formation. Defaults to ["FORMATION", "GROUP"].
        standardize_level_names (bool, optional): whether to standardize formation
        or group names. Defaults to True.

    Returns:
        Dict[str, pd.DataFrame]: dictionary with keys being level and values being the
        calibration map in dataframe format
    """
    if levels is None:
        levels = ["FORMATION", "GROUP"]
    missing_curves = [
        c
        for c in curves + location_curves + levels + [id_column]
        if c not in df.columns
    ]
    if len(missing_curves) > 0:
        raise ValueError(f"Missing necessary curves in dataframe: {missing_curves}")

    if standardize_level_names and any(((c in ["FORMATION", "GROUP"]) for c in levels)):
        for level in levels:
            df[level] = df[level].apply(standardize_group_formation_name)

    level_tables = {level: None for level in levels}
    for level in levels:
        data = []
        for w in df[id_column].unique():
            df_well = df[df[id_column] == w]
            for g, s in df_well.groupby(level, dropna=True):
                new_row = [
                    w,
                    g,
                    *getattr(
                        s[curves + location_curves].dropna(how="all"), mode
                    )().to_numpy(),
                ]
                data.append(new_row)
        level_tables[level] = pd.DataFrame(
            data, columns=["well_name", level, *curves, *location_curves]
        )
    return level_tables


def get_calibration_values(
    df: pd.DataFrame,
    curves: List[str],
    location_curves: List[str],
    level: str,
    mode: str,
    id_column: str,
    distance_thres: float = 99999.0,
    calibration_map: Optional[pd.DataFrame] = None,
    standardize_level_names: bool = True,
) -> Dict[str, pd.DataFrame]:
    """
    Get calibration map and fill na values (if any) for that well
    in calibration maps from closeby wells.

    Args:
        df (pd.DataFrame): dataframe
        curves (List[str]): list of curves to take into account for maps
        location_curves (List[str]): which curves to consider for calculating the distance between wells
        level (str):  how to group samples in a well, typically per group or formation
        mode (str): any method supported in pandas dataframe for representing the curve,
        such as median, mean, mode, min, max, etc.
        id_column (str): column with well names
        distance_thres (float, optional): threshold for indicating a well is to
        far to be considered close enough. Defaults to 99999.0.
        calibration_map (pd.DataFrame, optional): calibration map for the level. Defaults to None.
        standardize_level_names (bool, optional): whether to standardize formation
        or group names. Defaults to True.

    Returns:
        Dict[str, pd.DataFrame]: _description_
    """
    missing_curves = [
        c for c in curves + location_curves + [level, id_column] if c not in df.columns
    ]
    if len(missing_curves) > 0:
        raise ValueError(f"Missing necessary curves in dataframe: {missing_curves}")

    if standardize_level_names and level in ["FORMATION", "GROUP"]:
        df[level] = df[level].apply(standardize_group_formation_name)

    # get closest wells based on location curves
    def get_closest_wells(
        w_name: str,
        well_measures: pd.DataFrame,
        location_curves: List[str],
        calib_map: pd.DataFrame,
        distance_thres: float,
    ) -> Any:
        non_nan_cols = well_measures[location_curves].dropna().index.tolist()
        well_location = well_measures[non_nan_cols].to_numpy()
        nona_rows = calib_map[non_nan_cols].dropna().index
        calib_locations = calib_map.loc[nona_rows, :][non_nan_cols].to_numpy()
        if len(non_nan_cols) < len(location_curves):
            if len(non_nan_cols) == 0:
                warnings.warn(
                    f"There are no valid values for {location_curves}"
                    "in well {w_name} for {well_measures.name}.",
                    stacklevel=2,
                )
                return []
            warnings.warn(
                f"Distance was calculated only with the following features "
                f"{non_nan_cols}, as the rest was missing in well {w_name} "
                f"for {well_measures.name}.",
                stacklevel=2,
            )
        # distance between well and all others:
        calib_map = calib_map.loc[nona_rows, :]
        calib_map["distance"] = np.linalg.norm(
            np.repeat([well_location], repeats=len(calib_map), axis=0)
            - calib_locations,
            axis=1,
        )
        calib_map = calib_map.loc[calib_map["distance"] <= distance_thres, :]
        # TODO: For now only returning 10 closests wells if more than 10 within
        # the distance threshold need to change this to radius based approach (maybe)
        closest_wells = calib_map.sort_values(by="distance")[id_column][:10]
        return closest_wells.tolist()

    # either get calibration from cdf if None or work on given map
    if calibration_map is None:
        # TODO get calibration map from CDF
        raise ValueError("Getting calibration map from CDF not yet implemented!")

    well_values = {}
    for well in df[id_column].unique():
        df_well = df[df[id_column] == well]
        well_properties: Union[Dict[str, float], pd.DataFrame] = {
            g: getattr(v[curves + location_curves].dropna(how="all"), mode)()
            for g, v in df_well.groupby(level)
        }
        well_properties = pd.DataFrame.from_dict(well_properties, orient="index")
        if well_properties.empty:
            warnings.warn(
                f"Well {well} could not be processed (all NaN)!",
                stacklevel=2,
            )
            continue

        # go through each level value, and find closest well
        for i in well_properties.index:
            if not any(well_properties.loc[i, curves].isna()):
                continue
            mask = (calibration_map[id_column] != well) & (calibration_map[level] == i)
            tmp_calib_map = calibration_map.loc[mask, :].copy()
            if not len(tmp_calib_map) > 0:
                continue

            closest_wells = get_closest_wells(
                well,
                well_properties.loc[i],
                location_curves,
                tmp_calib_map,
                distance_thres,
            )
            cwells_map = tmp_calib_map[tmp_calib_map[id_column].isin(closest_wells)]

            if len(closest_wells) == 0:
                continue
            for c in closest_wells:
                well_properties.update(
                    cwells_map.loc[
                        cwells_map[id_column] == c, [level, *curves]
                    ].set_index(level),
                    overwrite=False,
                )
                if all(well_properties.loc[i, curves].notna()):
                    break
        well_values[well] = well_properties
    return well_values


def calculate_sampling_rate(array: pd.Series, max_sampling_rate=1):
    """
    Calculates the sampling rate of an array by calculating the weighed
    average diff between the array's values.

    Args:
        array (pd.Series): The array for which the sampling rate should be calculated
        max_sampling_rate: The maximum acceptable sampling rate above which the
            the calculated sampling rates should not be included in the weighted
            average calculation (defined in unit length/sample e.g. m). Defaults
            to max 1 m per sample (where m is the assumed unit of the provided array)
    """
    if array.empty or array.isna().all():
        raise ValueError(
            "The provided array is empty or contains only NaNs! Cannot calculate sampling rate!"
        )
    diffs = pd.Series(np.diff(array.to_numpy())).value_counts(normalize=True)
    # Ensure big holes in the index don't affect the weighted average
    # Asumming 1 is a good enough threshold for now
    diffs.loc[diffs.index.to_series().abs().gt(max_sampling_rate)] = np.nan
    sampling_rate = (diffs * diffs.index).sum()
    return sampling_rate


def squared_euclidean_distance(
    point_a: npt.NDArray[np.float64], point_b: npt.NDArray[np.float64]
) -> Any:
    """
    Returns the square of the Euclidean distance between two points

    Arguments:
        point_a (np.ndarray): The first point as [depth, x, y]
        point_b (np.ndarray): The second point as [depth, x, y]

    Returns:
        distance (float): The square of the Euclidean distance between point_a
                          and point b
    """
    return np.linalg.norm(point_a - point_b) ** 2


def estimate_parameter(
    depth: List[float],
    x: List[float],
    y: List[float],
    formation: List[str],
    group: List[str],
    parameter_train: List[float],
    depth_train: List[float],
    x_train: List[float],
    y_train: List[float],
    formation_train: List[str],
    group_train: List[str],
    distance_function: Callable[
        [npt.NDArray[np.float64], npt.NDArray[np.float64]], Any
    ] = squared_euclidean_distance,
) -> List[float]:
    """
    Estimates a parameter at given coordinates and zones based on a calibration list of
    parameters with corresponding coordinates and zones.

    Arguments:
        depth (List[float]): List of depths where parameter will be estimated
        x (List[float]): List of x-coordinates where parameter will be estimated
        y (List[float]): List of y-coordinates where parameter will be estimated
        formation (List[str]): List of formations where parameter will be estimated
        group (List[str]): List of groups where parameter will be estimated
        parameter_train (List[float]): Calibration parameter values
        depth_train (List[float]): List of depths for calibration points
        x_train (List[float]): List of x-coordinates for calibration points
        y_train (List[float]): List of y-coordinates for calibration points
        formation_train (List[str]): List of formations for the calibration points
        group_train (List[str]): List of groups for the calibration points
        distance_function (Callable([np.ndarray, np.ndarray], float)): Distance function
                    to use between points in [depth, x, y]

    Return:
        parameters (List[float]): Estimates of the parameter at the given points
    """
    df = pd.DataFrame({
        "DEPTH": depth_train,
        "X": x_train,
        "Y": y_train,
        "FORMATION": formation_train,
        "GROUP": group_train,
        "PARAMETER": parameter_train,
    })
    parameters = []
    for i in range(len(x)):
        # Filter on points in the same formation
        df_compare = df.loc[df.FORMATION == formation[i]]
        if df_compare.shape[0] == 0:
            # If not enough points of matching formation, go for groups
            df_compare = df.loc[df.GROUP == group[i]]
            if df_compare.shape[0] == 0:
                # If not enough points of matching group or formation, use all points
                df_compare = df
        # Compute the distance between the point and all points in
        # the dataframe of comparable calibration points
        point = np.array([depth[i], x[i], y[i]])
        calibration_points = df_compare[["DEPTH", "X", "Y"]].to_numpy()
        calibration_points_parameters = df_compare.PARAMETER.to_numpy()
        distances = np.apply_along_axis(distance_function, 1, calibration_points, point)
        # Remove any points that happen to be at zero distance
        zeros_indexes = [i for i, x in enumerate(distances) if x == 0.0]
        for ind in sorted(zeros_indexes, reverse=True):
            distances = np.delete(distances, ind)
            calibration_points_parameters = np.delete(
                calibration_points_parameters, ind
            )
        # Compute weighted average based on distance
        parameters.append(
            np.sum(1.0 / distances * calibration_points_parameters)
            / np.sum(1.0 / distances)
        )
    return parameters


def get_cognite_client(
    client_id: Optional[str] = None,
    client_secret: Optional[str] = None,
    permission_scope: str = "read",
    cognite_project_id: str = "akbp-subsurface",
    cognite_client_id: str = "mlpet",
) -> CogniteClient:
    """
    Helper function to create a CogniteClient instance.

    Args:
        client_id (str): Client id to authenticate the client with
        client_secret (str): Client secret to authenticate the client with
        cognite_project_id (str): The project ID to use for the CogniteClient, Defaults to akbp-subsurface
        cognite_client_id (str): The client ID to use for the CogniteClient
        persmission_scope (str): The permission scope to use for the CogniteClient, either "read" or "write", default to "read" (only relevant if using akerbp.mlops)

        Returns:
            CogniteClient: The created CogniteClient instance
    """
    permission = permission_scope.lower()
    if permission not in ["read", "write"]:
        raise ValueError(
            f"Invalid permission scope '{permission_scope}', must be either 'read' or 'write'"
        )

    cognite_client_id = "mlpet-client"
    base_url, tenant_id = None, None
    try:
        base_url = os.environ["COGNITE_OIDC_BASE_URL"]
    except KeyError as e:
        raise Exception(
            "Need to set COGNITE_OIDC_BASE_URL to initialize a cognite client"
        ) from e
    try:
        tenant_id = os.environ["COGNITE_TENANT_ID"]
    except KeyError as e:
        raise Exception(
            "Need to set COGNITE_TENANT_ID to initialize a cognite client"
        ) from e
    try:
        if client_id is None or client_secret is None:
            from akerbp.mlops.core.config import client_secrets as secrets

            client_id = secrets[f"id-{permission}"]
            client_secret = secrets[f"secret-{permission}"]
        else:
            pass
    except ModuleNotFoundError as e:
        raise Exception(
            f"Need to set client id and secret for permission scope {permission_scope} as environment variables to initialize a client"
        ) from e

    if client_id is None or client_secret is None:
        raise ValueError(
            "Both a client_id and corresponding client_secret must be provided to initialize a cognite client"
        )

    credentials = OAuthClientCredentials(
        token_url=f"https://login.microsoftonline.com/{tenant_id}/oauth2/v2.0/token",
        client_id=client_id,
        client_secret=client_secret,
        base_url=base_url,
        scopes=[f"{base_url}/.default"],
    )

    client_config = ClientConfig(
        client_name=cognite_client_id,
        project=cognite_project_id,
        credentials=credentials,
    )
    return CogniteClient(config=client_config)


def run_deployed_model(
    df: pd.DataFrame,
    id_column: str,
    keyword_arguments: Dict[str, Any],
    cdf_external_id: Optional[str] = None,
    **kwargs,
) -> pd.DataFrame:
    """
    Runs a deployed model on a dataframe.

    Args:
        df (pd.DataFrame): The dataframe to run the model on
        id_column (str): The column in the dataframe that contains the well names
        cdf_external_id (str): The external ID of the Cognite Data Fusion function
        keyword_arguments (Dict[str, Any]): Keyword arguments to pass to the model

    Returns:
        pd.DataFrame: The result of the model run
    """
    # We check that the input curves to the function will not have nans before sending them to the function
    df_ = df.copy()
    df_ = preprocessors.fillna_with_fillers(
        df_,
        num_filler=keyword_arguments["nan_numerical_value"],
        cat_filler=keyword_arguments["nan_textual_value"],
    )
    # Function call: prepare data as function payload description and fetch results
    # Ensure no NaNs in id_column
    if df[id_column].isna().any():
        raise ValueError(
            f"The id_column {id_column} contains NaNs, which is not allowed!"
        )
    in_data = {
        "input": [
            {
                "well": k,
                "input_logs": v.drop(columns=[id_column]).to_dict(orient="list"),
                "keyword_arguments": keyword_arguments,
            }
            for k, v in df_.groupby(id_column)
        ]
    }

    if cdf_external_id is not None:
        predictions = run_CDF_function(in_data, cdf_external_id, **kwargs)
    else:
        raise ValueError("No Cognite Data Fusion function was provided!")

    for well in predictions:
        pred = pd.DataFrame.from_dict(well)
        if "well_name" not in pred.columns:
            raise ValueError(
                "The result from the CDF function does not contain a 'well_name' column!"
            )
        elif len(well_name := pred["well_name"].unique()) > 1:
            raise ValueError(
                f"Multiple well names found in the payload response for one well: {well_name}!"
            )
        else:
            well_name = well_name[0]
        df_.loc[df_[id_column] == well_name, pred.columns] = pred.to_numpy()

    # Fill imputed values back to original
    df_ = preprocessors.set_as_nan(
        df_,
        numerical_value=keyword_arguments["nan_numerical_value"],
        categorical_value=keyword_arguments["nan_textual_value"],
    )

    return df_


def run_CDF_function(  # noqa: N802
    in_data: Dict[str, Any],
    cdf_external_id: str,
    client: Optional[CogniteClient] = None,
    return_file: bool = True,
    verbose: bool = False,
    **kwargs,
) -> pd.DataFrame:
    """
    Helper function to run a CDF function.

        Args:
            in_data: The payload to send to the CDF function
            external_id (str): The external ID to use for the function
            client (CogniteClient): The CogniteClient instance to use for the function
            return_file (bool): Whether to return the predictions as a CDF file link.
                Defaults to True.

        Returns:
            pd.DataFrame: The dataframe with the results of the function
    """
    # Create the CogniteClient instance
    if client is None:
        client = get_cognite_client(permission_scope="write")
    function = client.functions.retrieve(external_id=cdf_external_id)
    if function is None:
        raise ValueError(
            f"No function with external ID {cdf_external_id} found in Cognite!"
        )
    in_data["return_file"] = return_file
    # Create an RSA key pair to encrypt the results in the function
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
    )
    public_key = private_key.public_key()
    pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo,
    )
    in_data["public_key"] = pem.decode()

    call = function.call(in_data, wait=True)
    results = call.get_response()
    if results is None:
        raise ValueError(
            f"No response was returned from the CDF function with external ID {cdf_external_id} for call with id {call.id}!"
        )
    if results["status"] == "error":
        keys = [k for k in list(results) if "message" in k.lower()]
        if keys:
            raise ValueError(f"Function returned an error: {results[keys[0]]}")
        else:
            raise ValueError(f"Function returned an error: {results}")
    if verbose:
        logs = call.get_logs()
        if logs:
            print(logs.to_text(with_timestamps=True))
        else:
            warnings.warn(
                f"No logs were returned from the CDF function call {call.id}!",
                stacklevel=2,
            )

    if return_file:
        ciphertext = client.files.download_bytes(external_id=results["prediction_file"])
        encrypted = results.get("data_encrypted", False)
        if encrypted:
            print("Decrypting predictions received from Cognite!")
            encrypted_key = base64.b64decode(results["encrypted_key"].encode())
            key = private_key.decrypt(
                encrypted_key,
                asym_padding.OAEP(
                    mgf=asym_padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            algo = algorithms.AES(key)
            decryptor = Cipher(algo, modes.CBC(b"1234567890123456")).decryptor()
            padded_data = decryptor.update(ciphertext) + decryptor.finalize()
            unpadder = padding.PKCS7(algo.block_size).unpadder()
            content = unpadder.update(padded_data) + unpadder.finalize()
        else:
            content = ciphertext
        predictions = json.loads(content)
    else:
        predictions = results["prediction"]

    return predictions
