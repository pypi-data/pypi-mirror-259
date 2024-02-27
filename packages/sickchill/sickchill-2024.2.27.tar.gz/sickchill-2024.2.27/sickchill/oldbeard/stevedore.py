from subliminal.extensions import RegistrableExtensionManager

clients = RegistrableExtensionManager(
    "oldbeard.clients",
    [
        "deluge = oldbeard.clients.deluge:Client",
        "deluged = oldbeard.clients.deluged:Client",
        "download_station = oldbeard.clients.download_station:Client",
        "mlnet = oldbeard.clients.mlnet:Client",
        "qbittorrent = oldbeard.clients.qbittorrent:Client",
        "putio = oldbeard.clients.putio:Client",
        "rtorrent = oldbeard.clients.rtorrent:Client",
        "transmission = oldbeard.clients.transmission:Client",
        "utorrent = oldbeard.clients.utorrent:Client",
    ],
)

providers = RegistrableExtensionManager(
    "oldbeard.providers",
    [
        "hdspace = oldbeard.providers.hdspace:HDSpaceProvider",
        "ncore = oldbeard.providers.ncore:NcoreProvider",
        "tntvillage = oldbeard.providers.tntvillage:TNTVillageProvider",
        "rarbg = oldbeard.providers.rarbg:RarbgProvider",
        "elitetorrent = oldbeard.providers.elitetorrent:EliteTorrentProvider",
        "hd4free = oldbeard.providers.hd4free:HD4FreeProvider",
        "horriblesubs = oldbeard.providers.horriblesubs:HorribleSubsProvider",
        "limetorrents = oldbeard.providers.limetorrents:LimeTorrentsProvider",
        "cpasbien = oldbeard.providers.cpasbien:CpasbienProvider",
        "bjshare = oldbeard.providers.bjshare:BJShareProvider",
        "tvchaosuk = oldbeard.providers.tvchaosuk:TVChaosUKProvider",
        "eztv = oldbeard.providers.eztv:EZTVProvider",
        "shazbat = oldbeard.providers.shazbat:ShazbatProvider",
        "scc = oldbeard.providers.scc:SCCProvider",
        "thepiratebay = oldbeard.providers.thepiratebay:ThePirateBayProvider",
        "torrent_paradise = oldbeard.providers.torrent_paradise:Provider",
        "nyaa = oldbeard.providers.nyaa:NyaaProvider",
        "bitcannon = oldbeard.providers.bitcannon:BitCannonProvider",
        "magnetdl = oldbeard.providers.magnetdl:MagnetDLProvider",
        "hdtorrents_it = oldbeard.providers.hdtorrents_it:HDTorrentsProvider_IT",
        "skytorrents = oldbeard.providers.skytorrents:SkyTorrents",
        "xthor = oldbeard.providers.xthor:XThorProvider",
        "norbits = oldbeard.providers.norbits:NorbitsProvider",
        "yggtorrent = oldbeard.providers.yggtorrent:YggTorrentProvider",
        "torrentbytes = oldbeard.providers.torrentbytes:TorrentBytesProvider",
        "btn = oldbeard.providers.btn:BTNProvider",
        "demonoid = oldbeard.providers.demonoid:DemonoidProvider",
        "tokyotoshokan = oldbeard.providers.tokyotoshokan:TokyoToshokanProvider",
        "speedcd = oldbeard.providers.speedcd:SpeedCDProvider",
        "kat = oldbeard.providers.kat:KatProvider",
        "scenetime = oldbeard.providers.scenetime:SceneTimeProvider",
        "alpharatio = oldbeard.providers.alpharatio:AlphaRatioProvider",
        "hounddawgs = oldbeard.providers.hounddawgs:HoundDawgsProvider",
        "hdbits = oldbeard.providers.hdbits:HDBitsProvider",
        "pretome = oldbeard.providers.pretome:PretomeProvider",
        "binsearch = oldbeard.providers.binsearch:BinSearchProvider",
        "morethantv = oldbeard.providers.morethantv:MoreThanTVProvider",
        "torrentz = oldbeard.providers.torrentz:TorrentzProvider",
        "archetorrent = oldbeard.providers.archetorrent:ArcheTorrentProvider",
        "hdtorrents = oldbeard.providers.hdtorrents:HDTorrentsProvider",
        "immortalseed = oldbeard.providers.immortalseed:ImmortalseedProvider",
        "ilcorsaronero = oldbeard.providers.ilcorsaronero:ilCorsaroNeroProvider",
        "iptorrents = oldbeard.providers.iptorrents:IPTorrentsProvider",
        "torrent9 = oldbeard.providers.torrent9:Torrent9Provider",
        "newpct = oldbeard.providers.newpct:newpctProvider",
        "filelist = oldbeard.providers.filelist:FileListProvider",
        "abnormal = oldbeard.providers.abnormal:ABNormalProvider",
        "torrentproject = oldbeard.providers.torrentproject:TorrentProjectProvider",
        "danishbits = oldbeard.providers.danishbits:DanishbitsProvider",
        "omgwtfnzbs = oldbeard.providers.omgwtfnzbs:OmgwtfnzbsProvider",
        "gimmepeers = oldbeard.providers.gimmepeers:GimmePeersProvider",
        "nebulance = oldbeard.providers.nebulance:NebulanceProvider",
        "torrentday = oldbeard.providers.torrentday:TorrentDayProvider",
        "torrentleech = oldbeard.providers.torrentleech:TorrentLeechProvider",
        "zamunda = oldbeard.providers.zamunda:ZamundaProvider",
    ],
)

notifiers = RegistrableExtensionManager(
    "oldbeard.notifiers",
    [
        "plex = oldbeard.notifiers.plex:Notifier",
        "synoindex = oldbeard.notifiers.synoindex:Notifier",
        "telegram = oldbeard.notifiers.telegram:Notifier",
        "trakt = oldbeard.notifiers.trakt:Notifier",
        "join = oldbeard.notifiers.join:Notifier",
        "growl = oldbeard.notifiers.growl:Notifier",
        "emby = oldbeard.notifiers.emby:Notifier",
        "pushbullet = oldbeard.notifiers.pushbullet:Notifier",
        "nmjv2 = oldbeard.notifiers.nmjv2:Notifier",
        "tweet = oldbeard.notifiers.tweet:Notifier",
        "growl = oldbeard.notifiers.growl:Notifier",
        "pushalot = oldbeard.notifiers.pushalot:Notifier",
        "emailnotify = oldbeard.notifiers.emailnotify:Notifier",
        "prowl = oldbeard.notifiers.prowl:Notifier",
        "boxcar2 = oldbeard.notifiers.boxcar2:Notifier",
        "pytivo = oldbeard.notifiers.pytivo:Notifier",
        "boxcar2 = oldbeard.notifiers.boxcar2:Notifier",
        "nmj = oldbeard.notifiers.nmj:Notifier",
        "synologynotifier = oldbeard.notifiers.synologynotifier:Notifier",
        "matrix = oldbeard.notifiers.matrix:Notifier",
        "rocketchat = oldbeard.notifiers.rocketchat:Notifier",
        "trakt = oldbeard.notifiers.trakt:Notifier",
        "libnotify = oldbeard.notifiers.libnotify:Notifier",
        "rocketchat = oldbeard.notifiers.rocketchat:Notifier",
        "discord = oldbeard.notifiers.discord:Notifier",
        "pushbullet = oldbeard.notifiers.pushbullet:Notifier",
        # "twilio_notify = oldbeard.notifiers.twilio_notify:Notifier",
        "tweet = oldbeard.notifiers.tweet:Notifier",
        "synologynotifier = oldbeard.notifiers.synologynotifier:Notifier",
        "plex = oldbeard.notifiers.plex:Notifier",
        "discord = oldbeard.notifiers.discord:Notifier",
        "freemobile = oldbeard.notifiers.freemobile:Notifier",
        "slack = oldbeard.notifiers.slack:Notifier",
        "mattermost = oldbeard.notifiers.mattermost:Notifier",
        "mattermostbot = oldbeard.notifiers.mattermostbot:Notifier",
        "matrix = oldbeard.notifiers.matrix:Notifier",
        "synoindex = oldbeard.notifiers.synoindex:Notifier",
        "kodi = oldbeard.notifiers.kodi:Notifier",
        "nmjv2 = oldbeard.notifiers.nmjv2:Notifier",
        "emailnotify = oldbeard.notifiers.emailnotify:Notifier",
        "kodi = oldbeard.notifiers.kodi:Notifier",
        "pushalot = oldbeard.notifiers.pushalot:Notifier",
        "prowl = oldbeard.notifiers.prowl:Notifier",
        "pushover = oldbeard.notifiers.pushover:Notifier",
        "telegram = oldbeard.notifiers.telegram:Notifier",
        "pytivo = oldbeard.notifiers.pytivo:Notifier",
        "join = oldbeard.notifiers.join:Notifier",
        "pushover = oldbeard.notifiers.pushover:Notifier",
        "base = oldbeard.notifiers.base:Notifier",
        "emby = oldbeard.notifiers.emby:Notifier",
        "slack = oldbeard.notifiers.slack:Notifier",
        "freemobile = oldbeard.notifiers.freemobile:Notifier",
        "libnotify = oldbeard.notifiers.libnotify:Notifier",
        "nmj = oldbeard.notifiers.nmj:Notifier",
    ],
)

metadata = RegistrableExtensionManager(
    "sickchill.providers.metadata",
    [
        "mede8er = sickchill.providers.metadata.mede8er:Mede8erMetadata",
        "ps3 = sickchill.providers.metadata.ps3:PS3Metadata",
        "tivo = sickchill.providers.metadata.tivo:TIVOMetadata",
        "mede8er = sickchill.providers.metadata.mede8er:Mede8erMetadata",
        "tivo = sickchill.providers.metadata.tivo:TIVOMetadata",
        "mediabrowser = sickchill.providers.metadata.mediabrowser:MediaBrowserMetadata",
        "wdtv = sickchill.providers.metadata.wdtv:WDTVMetadata",
        "kodi = sickchill.providers.metadata.kodi:KODIMetadata",
        "wdtv = sickchill.providers.metadata.wdtv:WDTVMetadata",
        "kodi = sickchill.providers.metadata.kodi:KODIMetadata",
        "mediabrowser = sickchill.providers.metadata.mediabrowser:MediaBrowserMetadata",
        "ps3 = sickchill.providers.metadata.ps3:PS3Metadata",
    ],
)
