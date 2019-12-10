# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as LoremProvider


class Provider(LoremProvider):
    """
    Provider for generating Filipino lorem content

    Word list is based on the link below with some filtering, de-conjugating, and additional common words.

    Sources:
    - https://1000mostcommonwords.com/1000-most-common-filipino-words/
    """
    word_list = (
        'abo', 'abot', 'aga', 'agham', 'akin', 'aklat', 'ako', 'akyat', 'alam', 'alang-alang', 'alikabok', 'alin',
        'alok', 'alon', 'ama', 'amin', 'amoy', 'anak', 'ang', 'angkop', 'anim', 'ano', 'antas', 'apat', 'aral', 'araw',
        'ari-arian', 'asa', 'asawa', 'asin', 'aso', 'asukal', 'asul', 'at', 'atin', 'away', 'ay', 'ayos', 'baba',
        'babae', 'babaw', 'bagal', 'bagaman', 'bagay', 'bago', 'bagyo', 'bahagi', 'bahay', 'baka', 'bakal', 'bakasyon',
        'bakit', 'bakuran', 'balat', 'balde', 'balikat', 'banat', 'banda', 'bangka', 'bangko', 'bansa', 'barko', 'basa',
        'basehan', 'baso', 'bata', 'batas', 'batay', 'bato', 'bawas', 'bawat', 'bayad', 'bayan', 'baybayin', 'benta',
        'bente', 'berde', 'bibig', 'bigas', 'bigat', 'bigay', 'bigkas', 'bihira', 'bilang', 'bili', 'bilis', 'binata',
        'binibini', 'binti', 'biyahe', 'biyaya', 'boses', 'braso', 'buhangin', 'buhay', 'buhok', 'bukas', 'bulaklak',
        'bundok', 'buntot', 'buo', 'burol', 'butas', 'buti', 'buto', 'buwan', 'daan', 'dagat', 'dagdag', 'dahil',
        'dahilan', 'dala', 'dalaga', 'dalas', 'dalawampu', 'daliri', 'daloy', 'damit', 'damo', 'dapat', 'dati',
        'dating', 'digmaan', 'dilaw', 'disenyo', 'dito', 'doon', 'dugo', 'dyip', 'edad', 'eksakto', 'eksperimento',
        'elemento', 'enerhiya', 'epekto', 'eroplano', 'espesyal', 'estado', 'gabi', 'gala', 'galaw', 'galit', 'gamit',
        'gamot', 'gana', 'ganap', 'ganda', 'gas', 'gastos', 'gatas', 'gawa', 'gawin', 'gilid', 'giliw', 'ginang',
        'ginoo', 'ginto', 'gising', 'gitna', 'gubat', 'guhit', 'gulo', 'gulong', 'gusto', 'haba', 'habang', 'hakbang',
        'halaga', 'halalan', 'halaman', 'haligi', 'halimbawa', 'hambing', 'hanap', 'hanapbuhay', 'hanay', 'handa',
        'hanggan', 'hanggang', 'hangin', 'hardin', 'hati', 'hatid', 'hatol', 'hayop', 'higit', 'hila', 'hilaga',
        'hilera', 'himpapawid', 'hindi', 'hintay', 'hirap', 'hiwa', 'hiwalay', 'hugis', 'hula', 'huli', 'hulog',
        'humantong', 'husay', 'iba', 'ibabaw', 'ibig', 'ibon', 'ilalim', 'ilan', 'ilang', 'ilog', 'ilong', 'industriya',
        'ingay', 'inggit', 'init', 'inom', 'insekto', 'instrumento', 'inumin', 'ipon', 'isa', 'isda', 'isip', 'iskor',
        'isla', 'itim', 'itlog', 'ito', 'iwan', 'iyon', 'kaaway', 'kababaihan', 'kabayo', 'kabuuan', 'kaganapan',
        'kahit', 'kahon', 'kaibigan', 'kailangan', 'kailanman', 'kain', 'kaisa-isa', 'kakaiba', 'kalabit', 'kalagayan',
        'kalahati', 'kalakal', 'kalakalan', 'kalsada', 'kalye', 'kama', 'kamay', 'kampanilya', 'kampo', 'kanin',
        'kanluran', 'kanta', 'kanya', 'kapag', 'kapal', 'kapangyarihan', 'kapantay', 'kapatid', 'kapit-bahay',
        'kapital', 'kapitan', 'kapwa', 'karagatan', 'karamihan', 'karanasan', 'karaniwan', 'karapatan', 'karne',
        'kasalukuyan', 'kasama', 'kasanayan', 'kasangkapan', 'kasaysayan', 'kaso', 'katangian', 'katarungan', 'katawan',
        'katinig', 'katulad', 'katunayan', 'kawal', 'kaya', 'kaysa', 'kayumanggi', 'kilos', 'kinang', 'kinig', 'klase',
        'ko', 'kompanya', 'koponan', 'kopya', 'kotse', 'kuha', 'kulay', 'kumpleto', 'kung', 'kuskos', 'kuwento',
        'laban', 'lagay', 'lagda', 'lago', 'lahat', 'lahi', 'lakad', 'lakas', 'laki', 'lalim', 'lalo', 'laman',
        'lamang', 'lambak', 'lambot', 'lamig', 'landas', 'langis', 'langit', 'langoy', 'lapit', 'larawan', 'laro',
        'lason', 'lawa', 'lawak', 'layag', 'layo', 'leeg', 'libo', 'libre', 'ligaw', 'ligtas', 'liit', 'likas', 'likha',
        'likido', 'likod', 'lima', 'linaw', 'linggo', 'linis', 'linya', 'lipad', 'listahan', 'litaw', 'liwanag',
        'lubid', 'lugar', 'luma', 'lungsod', 'lupa', 'lupon', 'lutas', 'luwag', 'maaari', 'maaga', 'madali', 'maging',
        'maginoo', 'magkano', 'magulang', 'mahal', 'mahalaga', 'mahirap', 'maikli', 'mainam', 'mainit', 'mais',
        'makina', 'mali', 'maliban', 'manatili', 'manggagawa', 'mangyari', 'mangyaring', 'manipis', 'maniwala',
        'mansanas', 'mapa', 'marahil', 'marami', 'mas', 'masa', 'masyado', 'mata', 'may', 'mayroon', 'medyo', 'merkado',
        'mga', 'milyon', 'minahan', 'minuto', 'mukha', 'mula', 'muli', 'mundo', 'musika', 'na', 'naging', 'nais',
        'nakita', 'namin', 'nanay', 'nawala', 'nayon', 'ng', 'ngayon', 'ngipin', 'ngiti', 'ngunit', 'noon', 'numero',
        'oo', 'opisina', 'opo', 'oras', 'orihinal', 'pa', 'paa', 'paaralan', 'pabor', 'pabuya', 'pader', 'pagitan',
        'pakiramdam', 'paksa', 'palagi', 'palapag', 'pamamagitan', 'pamilya', 'panahon', 'panalo', 'pandiwa',
        'pangalan', 'panganib', 'pangarap', 'pangkat', 'pangmaramihang', 'pangngalan', 'pangunahin', 'pantig',
        'panuntunan', 'papel', 'para', 'paraan', 'pareho', 'pares', 'parirala', 'parisukat', 'partido', 'pasa',
        'pasiya', 'pasok', 'patakaran', 'patlang', 'patnubay', 'pato', 'payag', 'pera', 'pigil', 'pilak', 'pili',
        'pindot', 'pinto', 'piraso', 'pito', 'plano', 'port', 'posible', 'posisyon', 'problema', 'produkto', 'proseso',
        'prutas', 'pula', 'puno', 'punta', 'punto', 'pusa', 'puso', 'puti', 'puwang', 'puwersa', 'radyo', 'rehiyon',
        'resulta', 'sa', 'saan', 'sabay', 'sabi', 'sagot', 'sakahan', 'salamat', 'salamin', 'sali', 'salita', 'sama',
        'sampu', 'sandali', 'sang-ayon', 'sangay', 'sanggol', 'sapat', 'sapatos', 'sarili', 'sariwa', 'saya', 'sayaw',
        'sigaw', 'siglo', 'sigurado', 'sikat', 'sila', 'silangan', 'silya', 'simbolo', 'simula', 'singil', 'singsing',
        'sining', 'sira', 'sistema', 'siya', 'siyam', 'siyempre', 'solusyon', 'subok', 'sukat', 'sulat', 'sulok',
        'sulong', 'sumbrero', 'sundin', 'sundo', 'sunod', 'sunog', 'suot', 'suporta', 'suri', 'taas', 'taba', 'tagal',
        'tagumpay', 'tahanan', 'tahimik', 'tainga', 'takbo', 'takot', 'tala', 'talakay', 'talim', 'talo', 'talon',
        'tama', 'tandaan', 'tanggap', 'tanghali', 'tangi', 'tangkad', 'tanong', 'tao', 'taon', 'tapang', 'tapat',
        'tapon', 'tapos', 'tatlon', 'tatsulok', 'tawag', 'tawid', 'tayo', 'temperatura', 'timbang', 'timog', 'tinapay',
        'tinda', 'tindahan', 'tingin', 'tipon', 'tiyak', 'tono', 'totoo', 'trabaho', 'trak', 'tren', 'tubig', 'tugon',
        'tukoy', 'tuktok', 'tula', 'tulad', 'tulog', 'tulong', 'tuloy', 'tumba', 'tunay', 'tungkol', 'tungo', 'tunog',
        'turo', 'tuwa', 'tuwid', 'ugat', 'ulan', 'ulo', 'una', 'upo', 'upuan', 'uri', 'wala', 'walo', 'wika', 'yaman',
        'yelo',
    )