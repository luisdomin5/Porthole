import requests
import re

subjective = [
    'obvious',
    'certain',
    'abundant',
    'billions',
    'enough',
    'few',
    'full',
    'hundreds',
    'incalculable',
    'limited',
    'generally'
    'little',
    'many',
    'most',
    'millions',
    'numerous',
    'scarce',
    'some',
    'sparse',
    'substantial',
    'thousands',
    'big',
    'colossal',
    'fat',
    'gigantic',
    'great',
    'huge',
    'large',
    'little',
    'mammoth',
    'massive',
    'microscopic',
    'miniature',
    'petite',
    'puny',
    'scrawny',
    'short',
    'small',
    'tall',
    'teeny',
    'tiny',
    'ancient',
    'brief',
    'early',
    'fast',
    'future',
    'late',
    'long',
    'modern',
    'old',
    'old-fashioned',
    'prehistoric',
    'quick',
    'rapid',
    'short',
    'slow',
    'swift',
    'young',
    'wrong',
    'vast',
    'uninterested',
    'unimportant',
    'tender',
    'shy',
    'rich',
    'powerful',
    'poor',
    'poorly',
    'odd',
    'mushy',
    'mealy',
    'inexpensive',
    'important',
    'helpful',
    'hallowed',
    'gifted',
    'famous',
    'easy',
    'clever',
    'better',
    'aggressive',
    'zealous',
    'angry',
    'bewildered',
    'clumsy',
    'agreeable',
    'ambitious',
    'brave',
    'calm',
    'delightful',
    'eager',
    'faithful',
    'gentle',
    'happy',
    'jolly',
    'kind',
    'lively',
    'nice',
    'obedient',
    'polite',
    'proud',
    'silly',
    'thankful',
    'victorious',
    'witty',
    'wonderful',
    'unsightly',
    'unkempt',
    'ugly',
    'stocky',
    'skinny',
    'short',
    'shapely',
    'scruffy',
    'quaint',
    'plump',
    'plain',
    'muscular',
    'magnificent',
    'long',
    'handsome',
    'gorgeous',
    'glamorous',
    'flabby',
    'fit',
    'fancy',
    'elegant',
    'drab',
    'dazzling',
    'clean',
    'chubby',
    'beautiful',
    'bald',
    'attractive',
    'worried',
    'uptight',
    'thoughtless',
    'scary',
    'repulsive',
    'pitiful',
    'panicky',
    'obnoxious',
    'nervous',
    'mysterious',
    'lazy',
    'jealous',
    'itchy',
    'helpless',
    'grumpy',
    'fierce',
    'embarrassed',
    'defeated'
]

opinion = [
    ' I ',
    'I think',
    'I believe',
    'I feel',
    'I guess',
    'I agree',
    'I disagree',
    'Personally',
    'My impression',
    'In my opinion',
    'In my view',
    'In my eyes',
    'My favorite',
    'The best',
    'I strongly believe',
    'From my point of view',
    'It\'s my belief',
    'Based on what I know',
    'I am convinced',
    'Speaking for myself',
    'I know you will have to agree',
    'I am confident',
    'It seems to me',
    'In my opinion',
    'I am of the opinion',
    'I take the view',
    'My personal view is that',
    'In my experience',
    'As far as I',
    'As I see it',
    'As far as I know',
    'I might be wrong',
    'I am not mistaken',
    'It is claimed that',
    'I must admit that',
    'I cannot deny that',
    'I can imagine that',
    'I think',
    'I believe',
    'I suppose',
    'Personally, I think',
    'That is why I think',
    'I am sure',
    'I am certain',
    'I am convinced',
    'I am not certain',
    'I am not sure',
    'I am not convinced',
    'I have read that',
    'I am of mixed opinions',
    'I am of mixed opinions',
    'I have no opinion in this matter'
]

bullshit = [
    '10x',
    '24/7',
    ' ai ',
    'agile',
    'ambassador',
    'artificial intelligence',
    'at (your|their) fingertips?',
    'autonomous',
    'a[-/]b storying',
    'acquisition',
    'action items?',
    'act in time',
    'advantages?',
    'agents?',
    'aggregat(e|ion)',
    'accelerate',
    'all.in.one',
    'all.new',
    'amazing',
    'analytics?',
    'application service providers?',
    'as a service',
    'assets?',
    'astonishing',
    'authoritative',
    'automated',
    'augmented',
    'extended reality',
    'award.winning',
    'b2(b|c)',
    'back to the drawing board',
    'ball.?park',
    'band.aid',
    'bandwidth',
    '(benefit|gap) analysis',
    'bespoke',
    'best.in.class',
    'best.of.breed',
    'best.practice',
    'big.data',
    'big picture',
    'big thinkers?',
    'block.?chain',
    'blazing(ly)? fast',
    'boil the ocean',
    'bottom.line',
    'bottom.up',
    'boost(s|ing)?',
    'boundless',
    'brain.?storm(ing)?',
    'brain.?dump',
    'brand(s?|ing|ed)',
    'bright',
    'building.trust',
    'bulletproof',
    'burn.rates?',
    'business( cases| plans)',
    'buzz',
    'call to action',
    'capacity',
    'capabilit(y|ies)',
    'capitali(s|z)e',
    'centers? of excellence',
    'challenges?',
    'change agents?',
    'circle the wagons',
    'client-centered',
    'client-centric',
    'client-focused',
    'cloud',
    'cloud native',
    'cloudif(y|ication)',
    'collaborat(e|ion|ive)s?',
    'comfort( zone)?',
    'committee',
    'communicat(e|ion)s?',
    'company-employee.fit',
    'compelling',
    'competitive( advantage)?',
    'connected systems?',
    'complex(ity)?',
    'comprehensive',
    'connect the dots',
    'container orchestration',
    'containerizat(e|ion|ing)',
    'content management',
    'contextual(ly)?',
    'contingency plans?',
    'control groups?',
    'control plane',
    'convergence',
    'convergent',
    'conversions?',
    'core business',
    'core competenc(y|ies)',
    'core.to.edge',
    'cosmic',
    'cost-effective',
    'cost/benefit',
    'cost control',
    'craftsmanship',
    'critical path',
    'crypto.currency',
    'crypto(?!graphy).\\w+',
    'crm',
    'cross.sell',
    'crowd.?(fund(s?|ed|ing)|sourc(ed|e|ing))',
    'customer obsession',
    'cutting.edge',
    'cyber',
    'dashboards?',
    'dashboarding',
    'data mining',
    'decentrali(s|z)ed',
    'de-?dupe',
    'deep dive',
    'deep learning',
    'delight',
    'deliverables?',
    'demographic',
    'demystify',
    'demystifying',
    'deployless',
    'devops',
    'digital transformation',
    'differentiation',
    'discover(y|ed)?',
    'distributed ledgers?',
    'disrupt(ive|tor|ion|er)?',
    'dollar.productive',
    'downsi(s|z)e',
    'drill down',
    'drink the kool-aid',
    'drop.?in',
    'drop the ball',
    'due dilligence',
    'dynamic(s|ally)?',
    'e-?(business|commerce|tailers)',
    'early.stage',
    'eas(y|ily)',
    'ecosystem(s)?',
    'efficien(t|cy)',
    'effortless(ly)?',
    'elastic',
    'elaboration',
    'elephant in the room',
    'elevator pitch(ing)?',
    'enabl(e|ing)',
    'emerging markets?',
    'empower(ing|ment|s)?',
    'enablement',
    'end of the day',
    'end.to.end',
    'engulf',
    'engag(e(d)|ing|ment)',
    'enhanced?',
    'enterprise',
    'erp',
    'estimate',
    'eta',
    'etched in stone',
    'evangelist',
    'evolution',
    'exceed expectations',
    'excellent',
    'exceptional',
    'exclusive(ly)?',
    'exhaustive',
    'expedite',
    'experiences',
    'experts?',
    'expertise',
    'exposure',
    'extraordinary',
    'facilitat(e|or)',
    'fast track',
    'fault.tolerant',
    'feeling excited',
    'first.rate',
    'first.to.market',
    'flexibility',
    'flux',
    'foot view',
    'forward-thinking',
    'four pillars',
    'frictionless',
    'front lines',
    'frustration[- ]free',
    'functional',
    'futurist',
    'full benefit',
    'future.proof',
    'game changer',
    'game plan',
    'behavioral',
    'global(ly)?',
    'go public',
    'go.to.market',
    'goals?',
    'god-speed',
    'going forward',
    'granular',
    'ground.?breaking',
    'growth',
    'grow',
    'guidance',
    'guru',
    'guarantee(d)?',
    'hackathon',
    'hacker( mindset)?',
    'happiness manage(ment|rs?)',
    'hardball',
    'heavy.lifting',
    'herding cats',
    'hidden.gem',
    'hidden.meaning',
    'high.level',
    '(high|mass).impact',
    'high quality',
    'highly.scalable',
    'hive ?mind',
    'hybrid environments?',
    'hyperautomation',
    'hyper.personalization',
    'hyperconverged',
    'hyperscal(e|ed|ing)',
    'holistic',
    'ideathon',
    'ideation',
    'impactful',
    'impeccable',
    'in( |-)a( |-)nutshell',
    'incent',
    'incentivi(s|z)e',
    'increase the odds',
    'incredibl(e|y)',
    '(inflat|redeem)able value',
    'influencers?',
    'influx',
    'innovat(e|ed|ion|ive|ing|or)s?',
    'inspir(e|ing|ation)',
    'insights?',
    'integrat(e|ed|ion)s?',
    'internet[- ]of[- ]things',
    'intellectual property',
    'intuitive',
    'iot',
    'key results?',
    'kickstart(er|ed)?s?',
    'killjoy',
    'knowledge.(base|transfer|sharing)',
    'kpis?',
    'landing pages?',
    'lead the field',
    'leading',
    'leaders?',
    'leadership',
    'learnings',
    'legacy',
    'lessons learned',
    'level (the )? playing field',
    'level set',
    'leverag(e|ing)',
    'lifecycle',
    'low.hanging fruit',
    'look.(&|and).feel',
    'm2m',
    'machine learning',
    'made simple',
    'magical',
    'market (chang(er|ing)|leader|window|simplified|fit)',
    'market.ready',
    'marketing collateral',
    'maximi(s|z)e',
    'meaningful( client | )interactions?',
    'measurements?',
    'methodolog(y|ies)',
    'metrics',
    'middleware',
    'milestone',
    'military.grade encryption',
    'mind ?share',
    'mind ?shower',
    'mind-boggling',
    'mindset',
    '(mission|time).critical',
    'miracle',
    'ml',
    'moneti(s|z)e',
    'mov(e|ing) (fast|forward)',
    'multitask(ing?)',
    'multifaceted',
    'multi-?tenant(ed)?',
    'mvp',
    'negotiated',
    'networking',
    'new.economy',
    'new.breed',
    '(new|next|second).(level|gen|generation)',
    'nexus',
    'niches?',
    'ninja',
    'no-brainer',
    'non-traditional management',
    'objectives',
    'occupy the field',
    'off.site',
    'off.the.(radar|shelf)',
    'on board',
    'on.premises?',
    'on the (back end|radar screen|same page|house)',
    'one to one',
    'open the kimono',
    'opportunit(y|ies)',
    'outperform',
    'optimal',
    'orthogonal',
    'outcome(s)',
    'outstanding',
    'out(side)?.(of)?.the.(box|loop)',
    'outsourc(e|ed|ing)',
    '(total cost of )?ownership',
    'paradigms?( shift)?',
    'partner(ships?)?',
    'patents?',
    'people.focus(ed|sed)',
    'performance indicators',
    'perfect(ly)?',
    'personaliz(e|ed|ation)',
    'perspective',
    'phases?',
    'phased approach',
    'pipeline',
    'pioneers',
    'pivot',
    'planning horizon',
    'platforms?',
    'plethora',
    'plug.?in',
    'potentials?',
    'powerful',
    'prioriti(s|z)ed?',
    'proactive',
    'problem space',
    'processes',
    'profit(ability)?',
    'promotion',
    'promotional collateral',
    'prominent',
    'promise',
    'proprietary',
    'proof.of.concept',
    'prove(n|d)?',
    'purpose.built',
    'push the envelope',
    'push.back',
    'production.ready',
    'productivity',
    'pushing on open doors',
    'quick wins?',
    'rais(e|ing) the bar',
    'ramp.up',
    'ravishing',
    '(reaping )(tangible )rewards',
    'relationship management',
    'responsive',
    'engage(ments?)?',
    'reach out',
    'reactivation',
    'real.time',
    'real.world',
    'reconfigure',
    'redefin(e|ed|ing)',
    'red flags?',
    'reengineering',
    'reimagin(e|ed|ing)',
    'reinvent(ing)? the(.square)? wheel',
    'reinvigorate',
    'relevance',
    'repurpose',
    'resilien(ce|cy|t)',
    'resource allocation',
    'restructuring',
    'retention',
    'return on investment',
    'results',
    'reus(e|ability)',
    'revenue',
    'reverse.engineer',
    'revisit',
    'revolution',
    'revolutionary',
    'reward(ing)?(.experience)?',
    'rich',
    'road ?map',
    'robust',
    'rock.?star',
    'roi',
    'run the numbers',
    '(s|p)aas',
    'sacrific(e|es|ing)',
    'scal(e|es|ing|ability)',
    'high availability',
    'scenarios?',
    'scope',
    'scrum( master)?',
    'seamless',
    'secret sauce',
    'search engine optimization',
    'segments?',
    'self-managed team',
    'seo',
    '(serial )?entrepreneurs?',
    'serverless',
    'service mesh',
    'shareholder value',
    'significant(ly)?',
    'single-source responsibility',
    'skill ?sets?',
    'smart(er)?',
    'smoke (&|and) mirrors',
    'social(.media|.gaming|.networks?)',
    'solidality',
    'solutions?',
    'sophisticated',
    'soup to nuts',
    'sow',
    'spatial.computing',
    'stakeholders?',
    'start.up?',
    'statement of work',
    'state.of.the.art',
    'step.changes?',
    'sticky-?ness',
    'strateg(y|ic|ize|ise)',
    'streamlin(ed|e|ing)',
    'story points?',
    'success(ful)?',
    'super(critical|star|nova)',
    'sustainab(le|ility)',
    'synerg(y|ies|ized|i)',
    'systems?',
    'tailwinds?',
    'talented',
    'take offline',
    'talking points',
    'target (audience|group)',
    'targeted',
    'tasked',
    'tco',
    'team.building',
    'team.player',
    'teamwork',
    'technolog(y|ies)',
    'that being said',
    'thought.leader',
    'throughput',
    'time.to.awesome',
    'time.to.market',
    'timelines?',
    'top.down',
    'top.of.the.game',
    'total quality',
    'touch.base',
    'touchpoints?',
    'traction',
    'transform(ing|ative|ation(al))',
    'trends?',
    'true',
    'truths?',
    'turnkey',
    'ultimate',
    'up.to.speed',
    'up-?sell',
    'upside',
    'user.friendly',
    'user funnels?',
    'user.experience',
    'utili(s|z)(e|ation)',
    'uncover',
    'unicorn',
    'unique approach',
    'unlimited.holidays',
    'values?',
    'valueable',
    'value.add(ed)?',
    'venture',
    'venturing',
    'vertical market',
    'viral',
    'virtual(ization|isation)?',
    'visibility',
    'visio(n|nary)',
    'walk the talk',
    'wearable',
    'web.enabled',
    'win-win',
    'wisdom of crowds',
    'with due respect',
    'with ease',
    'wizards?',
    'workflows?',
    'workloads?',
    'workplaceless',
    'workspace',
    'world.?class',
    'world a better place',
    'wow.factor',
    'you\'ve never seen (a|an) \\w+',
    'zeitgeist',
    'zenith'
]

storyRaw = open("story.txt","r")
story = storyRaw.read()
storyRaw.close()
story = story.strip()

story = re.findall('<p>.+?</p>',story)
story= listToStr = ' '.join([str(elem) for elem in story])
if (len(story) < 500):
    story = re.findall('</cite>.+?\.</div></div>',story)
story = re.sub('<a href=.+?<em>', '', story)
story = re.sub('data-cfemail=.+?<em>', '', story)
story = re.sub('<div class=".+?\"', '', story)
story = re.sub('data-ad-text=.+?>', '', story)
story = re.sub('<div data.+?>', '', story)
story = re.sub('<ul class=.+?>', '', story)
story = re.sub('"https.+?"', '', story)
story = re.sub('//.+?"', '', story)
story = re.sub('data-src.+?"', '', story)
story = re.sub('data-.+?/script', '', story)
story = re.sub('data-.+?"', '', story)
story = re.sub('class=".+?"', '', story)
story = re.sub('<div id=".+?"', '', story)
story = re.sub('<div.+?alt=', '', story)
story = re.sub('click".+?"', '', story)
story = re.sub('id=.+?>', '', story)
story = story.replace("<p>", "\n")
story = story.replace("</p>", "\n")
story = story.replace("    ", "\n")
story = story.replace("<h1>", "\n")
story = story.replace("<h2>", "\n")
story = story.replace("<h3>", "\n")
story = story.replace("</h1>", "")
story = story.replace("</h2>", "")
story = story.replace("</h3>", "")
story = story.replace("<strong>", "    ")
story = story.replace("</strong>", "")
story = story.replace("</ul> >", "")
story = story.replace("<span class=", "")
story = story.replace("<em>", "")
story = story.replace("</em>", "")
story = story.replace("</a>", "")
story = story.replace("</ul", "")
story = story.replace("&ldquo;", "\"")
story = story.replace("&rdquo;", "\"")
story = story.replace("<a href=", "")
story = story.replace("target=", "")
story = story.replace("</cite>", "")
story = story.replace("</div> >", "")
story = story.replace("</div>", "")
story = story.replace("</span>=", "")
story = story.replace("<span>=", "")
story = story.replace("</span>", "")
story = story.replace("<span>", "")
story = story.replace("\"_blank\"", "")
story = story.replace("\">", "\"")
story = story.replace(">", "")
story = story.replace("\"\"", "")

quotes = []
point = 0
while (point < (len(story)-1)):
    start = story.find('"', point)
    end = (story.find('"', start + 1) + 1)
    if (start == -1):
        break
    quotes.append(story[start : end])
    point = end + 1

story = re.sub('".+?"', 'insertQuote', story)

num_subjective = 0
num_opinion = 0
num_bullshit = 0

for term in subjective:
    num_subjective += story.count(term)
    story = story.replace(term, '\033[0;34m' + term + '\033[0m')
    
for term in opinion:
    num_opinion += story.count(term)
    story = story.replace(term, '\033[0;32m' + term + '\033[0m')
    
for term in bullshit:
    num_bullshit += story.count(term)
    story = story.replace(term, '\033[0;31m' + term + '\033[0m')

for quote in quotes:
    story = story.replace('insertQuote', quote, 1)

print story
print "Subjective occurences:", "\033[0;34m", num_subjective, "\033[0m", " Opinionated occurences:", "\033[0;32m", num_opinion, "\033[0m", " Bullshit occurences:", "\033[0;31m", num_bullshit, "\033[0m"
