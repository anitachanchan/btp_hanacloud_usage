"""
Tool loader for BTP Usage Agent.

This agent does NOT use MCP / Agent Gateway.
It directly calls the SAP UAS Reporting API using OAuth2 client credentials
stored in the local .env file.

Both endpoints (/reports/v1/subaccountUsage and /reports/v1/monthlyUsage) are
part of the same UAS API and share the same base URL and OAuth2 credentials,
so all tools live in a single module: uas_tool.py.

To add more tools, import and add them to the list returned by get_mcp_tools().
"""

import logging

from uas_tool import (
    # ── Global account monthly usage ─────────────────────────────────────────
    list_subaccounts,
    get_global_account_monthly_usage,
    # ── Subaccount daily usage ────────────────────────────────────────────────
    get_btp_usage,
    get_btp_services_summary,
    get_aicore_model_cu_usage,
    simulate_aicore_cu_eom_forecast,
    detect_aicore_cu_anomaly,
)

logger = logging.getLogger(__name__)

_UAS_TOOLS = [
    # ── Global account discovery & monthly reporting ──────────────────────────
    # Call list_subaccounts first to discover available subaccount IDs,
    # then pass a subaccount ID to get_btp_usage for daily detail.
    list_subaccounts,
    get_global_account_monthly_usage,
    # ── Subaccount daily usage (UAS /reports/v1/subaccountUsage) ─────────────
    get_btp_usage,
    get_btp_services_summary,
    get_aicore_model_cu_usage,
    simulate_aicore_cu_eom_forecast,
    detect_aicore_cu_anomaly,
]


async def get_mcp_tools(use_cache: bool = True) -> list:
    """Return the BTP UAS tools for the agent.

    Signature is kept compatible with the standard mcp_tools contract
    so agent_executor.py requires no changes.
    """
    logger.info("Loaded %d UAS tool(s): %s", len(_UAS_TOOLS), [t.name for t in _UAS_TOOLS])
    return _UAS_TOOLS
