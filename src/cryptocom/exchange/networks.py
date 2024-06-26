from .structs import Network

ACA_NETWORK = Network("ACA")
ADA_NETWORK = Network("ADA")
AKT_NETWORK = Network("AKT")
ALGO_NETWORK = Network("ALGO")
APT_NETWORK = Network("APT")
AR_NETWORK = Network("AR")
ASTRC_NETWORK = Network("ASTRC")
ATOM_NETWORK = Network("ATOM")
AVAX_NETWORK = Network("AVAX")
AVAXC_NETWORK = Network("AVAXC")
Arbitrum_NETWORK = Network("Arbitrum")
BAND_NETWORK = Network("BAND")
BCH_NETWORK = Network("BCH")
BEP2_NETWORK = Network("BEP2")
BNB_NETWORK = Network("BNB")
BTC_NETWORK = Network("BTC")
CKB_NETWORK = Network("CKB")
CRO_NETWORK = Network("CRO")
CRONOS_NETWORK = Network("CRONOS")
CSPR_NETWORK = Network("CSPR")
DGB_NETWORK = Network("DGB")
DOGE_NETWORK = Network("DOGE")
DOT_NETWORK = Network("DOT")
EGLD_NETWORK = Network("EGLD")
EOS_NETWORK = Network("EOS")
ETC_NETWORK = Network("ETC")
ETH_NETWORK = Network("ETH")
ETHW_NETWORK = Network("ETHW")
FIL_NETWORK = Network("FIL")
FLOW_NETWORK = Network("FLOW")
FTM_NETWORK = Network("FTM")
GLMR_NETWORK = Network("GLMR")
HBAR_NETWORK = Network("HBAR")
HNT_NETWORK = Network("HNT")
ICP_NETWORK = Network("ICP")
ICX_NETWORK = Network("ICX")
IOTX_NETWORK = Network("IOTX")
KAVA_NETWORK = Network("KAVA")
KLAY_NETWORK = Network("KLAY")
KSM_NETWORK = Network("KSM")
LSK_NETWORK = Network("LSK")
LTC_NETWORK = Network("LTC")
LUNA2_NETWORK = Network("LUNA2")
LUNC_NETWORK = Network("LUNC")
MATIC_NETWORK = Network("MATIC")
MINA_NETWORK = Network("MINA")
MOVR_NETWORK = Network("MOVR")
NANO_NETWORK = Network("NANO")
NEAR_NETWORK = Network("NEAR")
NEO_NETWORK = Network("NEO")
ONE_NETWORK = Network("ONE")
ONT_NETWORK = Network("ONT")
OP_NETWORK = Network("OP")
QTUM_NETWORK = Network("QTUM")
RUNE_NETWORK = Network("RUNE")
SC_NETWORK = Network("SC")
SDN_NETWORK = Network("SDN")
SGB_NETWORK = Network("SGB")
SOL_NETWORK = Network("SOL")
STRAX_NETWORK = Network("STRAX")
STX_NETWORK = Network("STX")
THETA_NETWORK = Network("THETA")
VET_NETWORK = Network("VET")
WAVES_NETWORK = Network("WAVES")
WAXP_NETWORK = Network("WAXP")
XLM_NETWORK = Network("XLM")
XRP_NETWORK = Network("XRP")
XTZ_NETWORK = Network("XTZ")
ZIL_NETWORK = Network("ZIL")


def all():
    return [
        value for name, value in globals().items() if isinstance(value, Network)
    ]
