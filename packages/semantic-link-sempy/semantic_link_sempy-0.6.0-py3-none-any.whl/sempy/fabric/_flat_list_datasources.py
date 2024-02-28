import pandas as pd
from uuid import UUID

from sempy.fabric._cache import _get_or_create_workspace_client
from sempy.fabric._utils import collection_to_dataframe
from sempy._utils._log import log

from typing import Optional, Union


@log
def list_datasources(
    dataset: Union[str, UUID],
    workspace: Optional[Union[str, UUID]] = None
) -> pd.DataFrame:
    """
    List all datasources in a dataset.

    Parameters
    ----------
    dataset : str or uuid.UUID
        Name or UUID of the dataset.
    workspace : str or uuid.UUID, default=None
        The Fabric workspace name or UUID object containing the workspace ID.
        Defaults to None which resolves to the workspace of the attached lakehouse
        or if no lakehouse attached, resolves to the workspace of the notebook.

    Returns
    -------
    pandas.DataFrame
        Dataframe listing all datasources.
    """
    workspace_client = _get_or_create_workspace_client(workspace)
    database = workspace_client.get_dataset(dataset)

    extraction_def = [
        ("Data Source Name",   lambda r: r.Name,              "str"),  # noqa: E272
        ("Account",            lambda r: r.Account,           "str"),  # noqa: E272
        ("Connection String",  lambda r: r.Connectionstring,  "str"),  # noqa: E272
        ("Impersonation Mode", lambda r: r.ImpersonationMode, "str"),  # noqa: E272
        ("Isolation",          lambda r: r.Isolation,         "str"),  # noqa: E272
        ("Account",            lambda r: r.Account,           "str"),  # noqa: E272
        ("Type",               lambda r: r.Type,              "str"),  # noqa: E272
        ("Provider",           lambda r: r.Provider,          "str"),  # noqa: E272
        ("MaxConnections",     lambda r: r.MaxConnections,    "str"),  # noqa: E272
        ("Description",        lambda r: r.Description,       "str"),  # noqa: E272
    ]

    collection = database.Model.DataSources

    return collection_to_dataframe(collection, extraction_def)
