"""
italricette — Article Generator
Run: python build_articles.py
"""

from pathlib import Path

BASE   = Path(__file__).parent
DOMAIN = "https://italricette.com"
SITE   = "italricette"
DATE   = "2026-04-27"

ARTICLES = [

  # ─── 1 ──────────────────────────────────────────────
  {
    "slug":        "spaghetti-carbonara",
    "title":       "Ricetta Spaghetti alla Carbonara — La Vera Ricetta Romana Originale",
    "desc":        "Impara la vera carbonara italiana: niente panna, niente scorciatoie. Solo uova, Pecorino, guanciale e spaghetti cotti alla perfezione. Pronta in 20 minuti.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Spaghetti alla Carbonara Autentici — La Vera Ricetta Romana",
    "intro":       "Dimentica la panna. La vera carbonara romana è una salsa setosa e ricca fatta con uova, Pecorino Romano e un goccio di acqua di cottura amidacea — nient'altro. Questa è la ricetta che i romani preparano davvero in casa, tramandata di generazione in generazione.",
    "prep":        "5 min", "cook": "15 min", "total": "20 min",
    "servings":    "2 porzioni", "calories": "~620", "difficulty": "Medio",
    "badge_text":  "20 Min",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "spaghetti carbonara, carbonara autentica, carbonara senza panna, pasta romana, ricetta carbonara originale",
    "cal_num":     "620", "protein": "28g", "fat": "26g", "carbs": "68g",
    "ingredients": [
      "200g spaghetti",
      "100g guanciale (o pancetta come sostituto)",
      "3 tuorli d'uovo grandi + 1 uovo intero",
      "60g Pecorino Romano, grattugiato finemente",
      "30g Parmigiano Reggiano, grattugiato finemente",
      "Pepe nero macinato fresco (quantità generosa)",
      "Sale solo per l'acqua della pasta",
    ],
    "steps": [
      "Porta a ebollizione una pentola grande d'acqua salata. Cuoci gli spaghetti fino a quasi al dente — finiranno di cuocere in padella.",
      "Taglia il guanciale a listarelle. Cuocilo in una padella fredda a fuoco medio finché il grasso si scioglie e i bordi diventano croccanti. Togli dal fuoco.",
      "In una ciotola, sbatti i tuorli, l'uovo intero, il Pecorino, il Parmigiano e una generosa dose di pepe nero macinato.",
      "Prima di scolare, conserva almeno 1 tazza di acqua di cottura. Scola gli spaghetti.",
      "Aggiungi gli spaghetti scolati direttamente nella padella con il guanciale (fuori dal fuoco). Mescola per insaporire nel grasso.",
      "Aggiungi il composto di uova e mescola subito vigorosamente, aggiungendo l'acqua di cottura un po' alla volta finché ottieni una salsa lucida e cremosa che avvolge ogni filo. Lavora velocemente — il calore residuo cuoce le uova senza farle stracciare.",
      "Impiatta subito con altro Pecorino e un'ultima macinata di pepe nero.",
    ],
    "tips": [
      "Non aggiungere mai la panna — non è carbonara.",
      "Lavora fuori dal fuoco quando aggiungi le uova per evitare che si stracchino.",
      "Tieni l'acqua di cottura a portata di mano — è fondamentale per la consistenza setosa.",
      "Usa uova a temperatura ambiente per una migliore emulsione.",
    ],
    "prose1_h2":   "Perché la Vera Carbonara Non Ha la Panna",
    "prose1":      """La vera carbonara è nata a Roma dopo la Seconda Guerra Mondiale, e la ricetta originale si basa interamente sulla magia dell'emulsione delle uova. Quando la pasta calda incontra le uova sbattute e l'acqua di cottura amidacea, si forma naturalmente una salsa setosa e vellutata. Aggiungere la panna rompe questa chimica e rende il piatto più pesante e meno ricco di sfumature. I cuochi romani sono appassionati su questo: niente panna, niente aglio, niente cipolla. Solo i quattro ingredienti di base preparati alla perfezione.""",
    "prose2_h2":   "Guanciale vs Pancetta: Fa Davvero la Differenza?",
    "prose2":      """Il guanciale (guancia di maiale stagionata) è la scelta tradizionale — il suo contenuto di grasso più elevato e il sapore più intenso fanno davvero la differenza. La pancetta è un sostituto perfettamente accettabile se il guanciale è difficile da trovare. Evita il bacon affumicato, che ha un sapore che stride con l'equilibrio delicato del piatto. Se sei in Italia, usa il guanciale senza esitazione.""",
    "img2_alt":    "Primo piano di spaghetti alla carbonara autentici con salsa all'uovo setosa e guanciale croccante",
    "prose3_h2":   "Conservazione e Riscaldamento",
    "prose3":      """La carbonara non si conserva bene — la salsa si rompe al riscaldamento. È pensata per essere consumata immediatamente appena tolta dal fuoco. Se devi riscaldarla, fallo molto delicatamente in padella a fuoco basso con un goccio d'acqua, mescolando continuamente. Non usare mai il microonde.""",
    "faqs": [
      ("Posso usare la pancetta invece del guanciale?",
       "Sì, ma il sapore sarà più affumicato e meno autentico. La pancetta è il miglior sostituto — è stagionata ma non affumicata, mantenendo il profilo aromatico più vicino alla ricetta romana originale."),
      ("Perché la mia carbonara si è trasformata in uova strapazzate?",
       "La padella o la pasta erano troppo calde quando hai aggiunto le uova. Togli sempre dal fuoco prima, poi aggiungi il composto di uova mescolando velocemente. Aggiungi acqua di cottura fredda per abbassare la temperatura se necessario."),
      ("Posso fare la carbonara senza Pecorino?",
       "Usa solo Parmigiano Reggiano se non trovi il Pecorino. Il sapore sarà più delicato e meno pungente, ma rimane comunque una pasta deliziosa. La sapidità e il carattere del Pecorino sono ciò che rende la carbonara autentica."),
      ("Quante uova devo usare per persona?",
       "Lo standard è 2 tuorli a persona più 1 uovo intero ogni 2 porzioni. Questo rapporto dona la salsa più ricca e stabile."),
      ("La carbonara è sicura con le uova semi-cotte?",
       "Le uova vengono cotte delicatamente dal calore della pasta — non rimangono mai crude. La salsa raggiunge una temperatura sicura durante la mantecatura. Usa uova fresche di alta qualità."),
    ],
  },

  # ─── 2 ──────────────────────────────────────────────
  {
    "slug":        "homemade-pizza-dough",
    "title":       "Migliore Impasto Pizza Fatto in Casa — Croccante, Gommoso, Perfetto",
    "desc":        "Questo semplice impasto con 5 ingredienti ti dà una crosta croccante e gommosa ogni volta. Nessuna impastatrice necessaria. Preparalo lo stesso giorno o la sera prima per risultati ancora migliori.",
    "tag":         "Lievitati",
    "tag_color":   "#e65100",
    "tag_bg":      "#fff3e0",
    "h1":          "Migliore Impasto per Pizza Fatto in Casa — Crosta Croccante e Perfetta",
    "intro":       "Cinque ingredienti. Una sola ciotola. La migliore pizza che tu abbia mai preparato in casa. Questa ricetta funziona per la pizza napoletana sottile, la pizza alta al tegame o qualsiasi via di mezzo. Padroneggia l'impasto, e la pizza night cambierà per sempre.",
    "prep":        "15 min", "cook": "12 min", "total": "1 ora 30 min",
    "servings":    "2 pizze", "calories": "~280/fetta", "difficulty": "Facile",
    "badge_text":  "5 Ingredienti",
    "cuisine":     "Italiana",
    "category":    "Lievitati",
    "keywords":    "impasto pizza fatto in casa, ricetta impasto pizza, pizza napoletana, impasto pizza facile, come fare la pizza",
    "cal_num":     "280", "protein": "8g", "fat": "4g", "carbs": "52g",
    "ingredients": [
      "500g farina 00 o farina di forza",
      "7g (1 bustina) lievito di birra secco istantaneo",
      "325ml acqua tiepida (38°C)",
      "10g sale fino marino",
      "15ml (1 cucchiaio) olio extravergine d'oliva",
    ],
    "steps": [
      "Unisci l'acqua tiepida e il lievito in una ciotola grande. Lascia riposare 5 minuti finché fa la schiuma (salta questo passaggio con il lievito istantaneo).",
      "Aggiungi farina, sale e olio. Mescola con una forchetta finché si forma un impasto grezzo, poi trasferiscilo su una superficie leggermente infarinata.",
      "Impasta per 8–10 minuti finché diventa liscio ed elastico. L'impasto deve tornare su quando lo premi con un dito.",
      "Forma una palla, mettila in una ciotola unta, coprila con pellicola. Fai lievitare a temperatura ambiente per 1–1,5 ore finché raddoppia. (Oppure metti in frigo tutta la notte per un sapore migliore.)",
      "Dividi in 2 palline uguali. Fai riposare 15 minuti prima di stendere — questo rilassa il glutine.",
      "Preriscalda il forno alla temperatura massima (250°C o più). Usa una pietra refrattaria o una teglia d'acciaio se le hai.",
      "Stendi l'impasto con le mani (non usare mai il mattarello). Condisci e cuoci 10–12 minuti finché la crosta è dorata e con le caratteristiche bolle.",
    ],
    "tips": [
      "La farina 00 dona l'impasto più morbido ed elastico — usa la farina di forza come alternativa.",
      "Non usare mai il mattarello — degassa l'impasto e uccide la crosta areata.",
      "La lievitazione lenta in frigo (24–72 ore) migliora drasticamente il sapore.",
      "Più il forno è caldo, meglio è. La pietra refrattaria vale davvero l'investimento.",
    ],
    "prose1_h2":   "Farina 00 vs Farina di Forza: Quale è Migliore?",
    "prose1":      """La farina 00 italiana è macinata finissima, il che crea un impasto incredibilmente liscio ed elastico che si stende magnificamente senza strapparsi. È lo standard a Napoli e produce la caratteristica crosta napoletana. La farina di forza ha più glutine e crea una crosta più gommosa e leggermente più densa — ottima per la pizza in stile New York. Entrambe funzionano bene. Usa quello che trovi, ma se vuoi il risultato italiano più autentico, cerca la farina 00.""",
    "prose2_h2":   "Lievitazione a Freddo: Il Segreto per un Sapore Straordinario",
    "prose2":      """L'impasto del giorno è buono. Quello a lievitazione lenta in frigo è straordinario. Conservare l'impasto in frigo per 24–72 ore rallenta la fermentazione, sviluppando sapori complessi che non puoi accelerare. La crosta diventa più saporita, leggermente acidula e sviluppa un colore migliore in forno. Se pianifichi la pizza per sabato, prepara l'impasto giovedì. La differenza è drastica.""",
    "img2_alt":    "Mani che stendono l'impasto per pizza fatto in casa mostrando la perfetta struttura del glutine",
    "prose3_h2":   "Conservazione e Congelamento dell'Impasto",
    "prose3":      """Le palline di impasto non cotto si conservano in frigo fino a 3 giorni o si congelano fino a 3 mesi. Congela in sacchetti con zip oliati dopo la prima lievitazione. Scongela in frigo tutta la notte, poi porta a temperatura ambiente 30 minuti prima di stendere. Puoi fare una grande quantità e avere sempre l'impasto pronto all'occorrenza.""",
    "faqs": [
      ("Posso fare l'impasto senza lievito?",
       "Sì — usa 2 cucchiaini di lievito per dolci al posto del lievito di birra. Mescola l'impasto, salta la lievitazione e cuoci subito. Il risultato è più simile a una focaccia che a una pizza tradizionale, ma funziona in emergenza e impiega solo 15 minuti."),
      ("Perché il mio impasto è appiccicoso?",
       "Un impasto leggermente appiccicoso è normale e in realtà auspicabile — mantiene la crosta leggera e ariosa. Evita di aggiungere troppa farina, che rende la crosta densa e dura. Le mani bagnate o un raschietto aiutano a gestire l'appiccicosità."),
      ("Posso usare la farina 0 invece della 00?",
       "Sì, la farina 0 funziona. L'impasto sarà leggermente meno elastico ma produce comunque una crosta molto buona. La farina di forza è un sostituto migliore della 0 se cerchi gommosità."),
      ("Quanto sottile devo stendere l'impasto?",
       "Per lo stile napoletano, stendi a circa 28–30 cm — centro sottile con bordo leggermente più spesso. Per la pizza al tegame, premi in una teglia unta e lascia riposare 20 minuti prima di condire."),
      ("Ho bisogno della pietra refrattaria?",
       "Non è necessaria, ma fa una differenza significativa. Una teglia pesante preriscaldata in forno per 30 minuti è la migliore alternativa gratuita. L'obiettivo è il contatto immediato con il calore elevato quando l'impasto tocca la superficie."),
    ],
  },

  # ─── 3 ──────────────────────────────────────────────
  {
    "slug":        "classic-tiramisu",
    "title":       "Ricetta Tiramisù Classico — L'Originale Italiano Senza Cottura",
    "desc":        "Il tiramisù italiano originale: savoiardi imbevuti di espresso, crema al mascarpone e cacao amaro. Niente panna montata, solo 6 ingredienti. Per 8 persone.",
    "tag":         "Dolci",
    "tag_color":   "#6a1b9a",
    "tag_bg":      "#f3e5f5",
    "h1":          "Tiramisù Classico Italiano — La Vera Ricetta Senza Cottura",
    "intro":       "Questo è il vero tiramisù — quello che gli italiani preparano davvero. Strati di savoiardi imbevuti di espresso, una ricca crema al mascarpone e un'abbondante spolverata di cacao amaro. Niente cottura, niente gelatina, niente scorciatoie. Solo i sei ingredienti che hanno reso questo dolce famoso in tutto il mondo.",
    "prep":        "25 min", "cook": "0 min", "total": "4 ore (frigo)",
    "servings":    "8 porzioni", "calories": "~420", "difficulty": "Facile",
    "badge_text":  "Senza Cottura",
    "cuisine":     "Italiana",
    "category":    "Dolci",
    "keywords":    "ricetta tiramisù, tiramisù classico, tiramisù autentico italiano, tiramisù senza cottura, come fare il tiramisù",
    "cal_num":     "420", "protein": "8g", "fat": "28g", "carbs": "34g",
    "ingredients": [
      "500g mascarpone (a temperatura ambiente)",
      "4 uova grandi, tuorli e albumi separati",
      "120g zucchero semolato",
      "300ml espresso forte, freddo",
      "30–40 savoiardi",
      "3 cucchiai di rum scuro o Marsala (facoltativo)",
      "Cacao amaro in polvere, per spolverare",
    ],
    "steps": [
      "Prepara l'espresso e lascialo raffreddare completamente. Aggiungi rum o Marsala se lo usi. Metti da parte in una ciotola bassa.",
      "Sbatti i tuorli con lo zucchero con le fruste elettriche per 4–5 minuti finché il composto diventa pallido, denso e a nastro (questo crea una base zabaione sicura).",
      "Aggiungi il mascarpone al composto di tuorli e mescola delicatamente con una spatola finché è liscio e senza grumi.",
      "In una ciotola pulita separata, monta gli albumi a neve ferma. Incorporali delicatamente alla crema al mascarpone in due aggiunte, con movimenti dal basso verso l'alto per mantenere l'aria.",
      "Immergi velocemente ogni savoiardo nell'espresso freddo per soli 1–2 secondi per lato. Devono essere umidi ma non inzuppati.",
      "Disponi uno strato di savoiardi imbevuti in una teglia da 23×33 cm. Spalma metà della crema al mascarpone sopra.",
      "Aggiungi un secondo strato di savoiardi imbevuti, poi la crema rimanente. Liscia la superficie.",
      "Copri e metti in frigo per almeno 4 ore — è ideale tutta la notte. Spolverizza abbondantemente con il cacao subito prima di servire.",
    ],
    "tips": [
      "Il mascarpone freddo fa grumi — portalo sempre a temperatura ambiente prima di usarlo.",
      "Solo 1–2 secondi di immersione — i savoiardi troppo imbevuti rendono il tiramisù molle e bagnato.",
      "La refrigerazione notturna fa solidificare perfettamente gli strati e intensifica i sapori.",
      "Spolverizza il cacao solo al momento di servire per evitare che assorba umidità.",
    ],
    "prose1_h2":   "Il Segreto per un Tiramisù Perfettamente Compatto",
    "prose1":      """L'errore più comune del tiramisù è inzuppare troppo i biscotti. Una veloce immersione — un secondo per lato — è tutto quello che serve. Assorbono umidità mentre il dolce si raffredda in frigo, e quando lo servi saranno perfettamente morbidi. Inzupparli troppo ti darà un pasticcio bagnato e sfaldante. L'altro segreto è la pazienza: almeno quattro ore in frigo, tutta la notte se possibile. È qui che avviene la magia — gli strati si fondono e si compattano in quei bellissimi strati distinti che sono il marchio di un gran tiramisù.""",
    "prose2_h2":   "Mascarpone vs Panna Montata: La Differenza",
    "prose2":      """Il tiramisù italiano autentico usa solo il mascarpone — mai la panna montata. Il mascarpone è un formaggio cremoso italiano ultra-ricco con un contenuto di grassi di circa il 75%, che dona alla crema una consistenza incredibilmente densa e lussuosa. Alcune ricette moderne sostituiscono la panna montata o mischiano entrambe, creando un risultato più leggero e meno ricco. Per l'esperienza del tiramisù classico, usa del vero mascarpone di un marchio italiano se riesci a trovarlo. La differenza di gusto e consistenza è significativa.""",
    "img2_alt":    "Tiramisù affettato che mostra i perfetti strati di crema al mascarpone e savoiardi imbevuti di espresso",
    "prose3_h2":   "Preparazione in Anticipo e Conservazione",
    "prose3":      """Il tiramisù è il dolce da preparare in anticipo per eccellenza. Si conserva perfettamente in frigo fino a 3 giorni coperto con pellicola. Il sapore migliora il secondo giorno. Puoi anche congelare le porzioni individuali fino a 1 mese — scongelale in frigo per alcune ore prima di servire. Non spolverizzare con il cacao fino al momento di servire.""",
    "faqs": [
      ("Posso fare il tiramisù senza alcol?",
       "Assolutamente. Ometti semplicemente il rum o il Marsala. Il tiramisù sarà comunque delizioso — il caffè e il mascarpone offrono più che abbastanza sapore. Puoi aggiungere un cucchiaino di estratto di vaniglia all'espresso per una maggiore profondità."),
      ("Quanto dura il tiramisù in frigo?",
       "Fino a 3 giorni coperto ermeticamente in frigo. Il sapore raggiunge il suo apice il secondo giorno mentre gli strati si amalgamano. Dopo 3 giorni i biscotti possono diventare troppo morbidi e la crema potrebbe iniziare a cedere."),
      ("Posso usare il formaggio spalmabile invece del mascarpone?",
       "Il formaggio spalmabile può funzionare come sostituto d'emergenza, ma il sapore e la consistenza saranno notevolmente diversi — più acidi e più sodi. Per il miglior risultato, usa sempre del vero mascarpone italiano."),
      ("Devo usare le uova crude?",
       "Questa ricetta usa un metodo semi-cotto: sbattere vigorosamente i tuorli con lo zucchero crea una base densa stile zabaione più sicura delle uova semplicemente crude. Per uova completamente cotte, scalda i tuorli e lo zucchero a bagnomaria a 70°C prima di sbattere."),
      ("Posso fare il tiramisù senza savoiardi?",
       "I savoiardi sono tradizionali, ma il pan di spagna tagliato a strisce funziona come sostituto. Alcune ricette usano i pavesini per una consistenza più fine. Evita le torte morbide — hai bisogno di qualcosa di abbastanza sodo da mantenere la forma dopo l'inzuppamento."),
    ],
  },


  # ─── 4 — cacio e pepe recipe ──────────────────────────────
  {
    "slug": "cacio-e-pepe-recipe",
    "title": "Ricetta Cacio e Pepe — La Guida Definitiva alla Ricetta Romana Autentica",
    "desc": "Padroneggia il vero cacio e pepe: 3 ingredienti, zero panna, perfetto ogni volta. Il piatto di pasta romano che mette in difficoltà anche i cuochi esperti — reso infallibile.",
    "tag": "Pasta", "tag_color": "#1565c0", "tag_bg": "#e3f2fd",
    "h1": "Cacio e Pepe — 3 Ingredienti, Autentico Romano, Perfetto Ogni Volta",
    "intro": "Tre ingredienti. Niente panna, niente burro (quasi). Niente scorciatoie. Il cacio e pepe è la più tecnicamente impegnativa delle quattro paste romane classiche — e la più gratificante quando riesce. Questa guida spiega esattamente perché va storto e come renderlo perfetto ogni singola volta.",
    "prep": "5 min", "cook": "15 min", "total": "20 min",
    "servings": "2 porzioni", "calories": "~580", "difficulty": "Medio",
    "badge_text": "3 Ingredienti", "cuisine": "Italiana", "category": "Pasta",
    "keywords": "ricetta cacio e pepe, cacio e pepe autentico, pasta romana, pasta cacio e pepe, come fare cacio e pepe",
    "cal_num": "580", "protein": "22g", "fat": "18g", "carbs": "80g",
    "ingredients": [
      "200g tonnarelli o spaghetti",
      "150g Pecorino Romano DOP, grattugiato finissimamente (microplane)",
      "2 cucchiaini di pepe nero in grani",
      "Sale per l'acqua della pasta (meno del solito — il Pecorino è molto salato)",
    ],
    "steps": [
      "Tosta i grani di pepe in una padella asciutta a fuoco medio per 60 secondi finché sono profumati. Macinali grossolanamente — vuoi texture, non polvere fine. Metti da parte nella padella.",
      "Cuoci la pasta in acqua salata (ma meno del solito). Conserva 1 tazza intera di acqua di cottura — è fondamentale.",
      "Grattugia il Pecorino con un microplane fino a ottenere una polvere fine — non scaglie. Mettilo in una ciotola.",
      "Aggiungi 2-3 cucchiai di acqua di cottura CALDA al Pecorino e mescola vigorosamente finché forma una pasta liscia e densa. La temperatura conta: troppo calda = grumi, troppo fredda = granulosa.",
      "Aggiungi un goccio di acqua di cottura alla padella con il pepe. Porta a leggero bollore. Aggiungi la pasta scolata al dente e mescola.",
      "Togli la padella completamente dal fuoco. Aggiungi la pasta di Pecorino. Mescola rapidamente e continuamente, aggiungendo acqua di cottura cucchiaio per cucchiaio finché ottieni una salsa lucida e cremosa. Lavora velocemente.",
      "Servi subito in ciotole calde. Aggiungi altro pepe macinato fresco e Pecorino extra.",
    ],
    "tips": [
      "Usa un microplane per il Pecorino — la grattugia grossa causa grumi.",
      "La padella deve essere SPENTA dal fuoco quando aggiungi la pasta di formaggio.",
      "Aggiungi l'acqua di cottura lentamente — troppa e la salsa diventa acquosa.",
      "Il tonnarello è la pasta tradizionale — uno spaghetto spesso e tagliato quadrato.",
    ],
    "prose1_h2": "Perché il Cacio e Pepe è così Difficile da Fare Bene",
    "prose1": "Il problema è fisico. Il Pecorino Romano ha un alto contenuto di grassi e sale che lo fa raggrumare e indurire quando esposto al calore elevato o all'umidità eccessiva. La differenza tra un cacio e pepe setoso da ristorante e un pasticcio grumoso è solitamente il controllo della temperatura e la tecnica. L'acqua di cottura non è solo un ingrediente — è l'emulsionante che tiene insieme tutto il piatto. Il suo contenuto di amido, la temperatura e il rapporto in cui viene aggiunta sono le variabili che separano il successo dal fallimento.",
    "prose2_h2": "Pecorino Romano vs Parmigiano: Quale Usare?",
    "prose2": "Il cacio e pepe tradizionale usa 100% Pecorino Romano — un formaggio di pecora pungente, salato e saporito. Alcune ricette moderne mescolano 70% Pecorino con 30% Parmigiano Reggiano per un sapore più delicato. Entrambe le versioni sono valide, ma quella romana purista è tutto Pecorino. Se hai mangiato cacio e pepe fatto solo con Parmigiano, hai assaggiato una versione più morbida e meno pungente. Usa il miglior Pecorino Romano DOP che riesci a trovare.",
    "img2_alt": "Primo piano di pasta cacio e pepe con salsa al Pecorino lucida e pepe nero macinato",
    "prose3_h2": "Conservazione e Riscaldamento",
    "prose3": "Il cacio e pepe va mangiato immediatamente — come tutti i piatti di pasta romani, non aspetta e non si riscalda bene. La salsa si indurisce e si raggruppa quando si raffredda. Se devi riscaldarla, fallo delicatamente in padella con un goccio d'acqua a fuoco bassissimo, mescolando continuamente.",
    "faqs": [
      ("Perché il mio cacio e pepe fa grumi?", "Il formaggio si è raggrumato perché la padella era troppo calda quando lo hai aggiunto, o l'hai aggiunto direttamente alla pasta senza fare prima una pasta di formaggio. Prepara sempre la pasta di Pecorino con acqua di cottura tiepida (non calda) prima, poi aggiungila fuori dal fuoco."),
      ("Posso usare il Parmigiano invece del Pecorino?", "Puoi, ma non è tradizionale. Il Parmigiano Reggiano si scioglie più facilmente ma ha un sapore più delicato. Se sei nuovo al cacio e pepe, un mix 50/50 è più indulgente mentre impari la tecnica."),
      ("Quale forma di pasta è migliore per il cacio e pepe?", "Il tonnarello è tradizionale — uno spaghetto spesso e quadrato tipico di Roma. Gli spaghetti normali o i rigatoni funzionano anche. La pasta deve essere amidacea — cuocila in meno acqua del normale per ottenere un'acqua di cottura più concentrata."),
      ("Ho bisogno del burro nel cacio e pepe?", "La ricetta romana originale usa solo pasta, Pecorino e pepe — niente burro. Alcune versioni moderne aggiungono un cucchiaio di burro per ricchezza, ma i puristi lo evitano. Prova prima senza."),
      ("Quanto pepe è troppo?", "Cacio e pepe significa letteralmente 'formaggio e pepe' — il pepe non è una guarnizione, è un ingrediente principale. Dovresti usarne più di quanto sembri comodo. 2 cucchiaini di pepe macinato grossolanamente per 2 porzioni è un buon punto di partenza."),
    ],
  },

  # ─── 5 — panna cotta recipe ───────────────────────────────
  {
    "slug": "panna-cotta-recipe",
    "title": "Ricetta Panna Cotta — Il Dolce Italiano Setoso con Solo 5 Ingredienti",
    "desc": "La panna cotta perfetta: setosa, appena rassodata, si scioglie in bocca. Solo 5 ingredienti, nessuna cottura, preparala il giorno prima. Con salsa di fragole o frutti di bosco.",
    "tag": "Dolci", "tag_color": "#6a1b9a", "tag_bg": "#f3e5f5",
    "h1": "Panna Cotta Perfetta — Setosa, Cremosa, 5 Ingredienti",
    "intro": "La panna cotta è il dolce italiano più elegante che puoi preparare con quasi nessuno sforzo. Solo panna, zucchero, vaniglia e una piccola quantità di gelatina — e basta. La panna cotta perfetta regge appena la forma, trema nel piatto e si scioglie completamente nel momento in cui tocca la lingua.",
    "prep": "10 min", "cook": "5 min", "total": "4 ore (frigo)",
    "servings": "6 porzioni", "calories": "~310", "difficulty": "Facile",
    "badge_text": "5 Ingredienti", "cuisine": "Italiana", "category": "Dolci",
    "keywords": "ricetta panna cotta, panna cotta italiana, panna cotta alla vaniglia, panna cotta con fragole, come fare la panna cotta",
    "cal_num": "310", "protein": "4g", "fat": "24g", "carbs": "22g",
    "ingredients": [
      "600ml panna fresca intera",
      "80g zucchero semolato",
      "1 bacca di vaniglia (oppure 1½ cucchiaino di estratto di vaniglia puro)",
      "7g (1 bustina) gelatina in polvere senza sapore",
      "3 cucchiai di acqua fredda (per far gonfiare la gelatina)",
      "— Per la salsa di fragole —",
      "250g fragole fresche (o frutti di bosco misti)",
      "2 cucchiai di zucchero · 1 cucchiaio di succo di limone",
    ],
    "steps": [
      "Versa la gelatina sui 3 cucchiai di acqua fredda in una ciotolina. Lascia riposare 5 minuti per farla gonfiare — assorbirà l'acqua e si rigonfierà.",
      "Taglia a metà la bacca di vaniglia e raschia i semi. Metti la panna, lo zucchero, la bacca di vaniglia e i semi in un pentolino.",
      "Scalda il composto di panna a fuoco medio, mescolando, finché lo zucchero si scioglie e la panna inizia a fumigare — NON lasciare bollire. Togli dal fuoco.",
      "Aggiungi la gelatina gonfia alla panna calda. Mescola fino a completo scioglimento. Rimuovi la bacca di vaniglia.",
      "Filtra attraverso un colino a maglie fini in una caraffa. Ungi leggermente 6 stampini o bicchieri con olio neutro. Versa il composto di panna in modo uniforme.",
      "Lascia raffreddare a temperatura ambiente, poi metti in frigo per almeno 4 ore — è ideale tutta la notte.",
      "Per la salsa: fai sobbollire fragole, zucchero e succo di limone per 5 minuti. Frulla o lascia a pezzi. Metti in frigo.",
      "Per sformare: passa un coltellino sottile lungo il bordo. Metti un piatto sopra e capovolgi con decisione. Versa la salsa sopra. Servi subito.",
    ],
    "tips": [
      "Usa la quantità minima di gelatina — la panna cotta deve tremare, non rimbalzare.",
      "Non far bollire la panna — cambia il sapore e può far rapprendere la gelatina in modo irregolare.",
      "Ungere leggermente gli stampini è il segreto per sformarla pulita.",
      "La refrigerazione notturna dà il miglior risultato, più uniforme.",
    ],
    "prose1_h2": "Il Segreto per la Consistenza Perfetta",
    "prose1": "La caratteristica distintiva di una grande panna cotta è la consistenza: deve essere appena rassodata, con un delicato tremolio che ti dice che si scioglierà nel momento in cui tocca la lingua. Il nemico della panna cotta perfetta è troppa gelatina. Molte ricette eccedono e producono un risultato gommoso che sa più di gelatina aromatizzata che di un raffinato dolce italiano. Il rapporto in questa ricetta usa la quantità minima di gelatina necessaria per sformare in modo pulito — non di più.",
    "prose2_h2": "Varianti di Sapore della Panna Cotta",
    "prose2": "La versione classica è alla vaniglia, ma la panna cotta è infinitamente versatile. Al caffè: aggiungi 2 tazzine di espresso alla panna. Al cioccolato: aggiungi 80g di cioccolato fondente dopo aver tolto dal fuoco. Al pistacchio: aggiungi 3 cucchiai di pasta di pistacchio. Al limoncello: aggiungi 2 cucchiai di limoncello e la scorza di 1 limone. Ogni variante segue la stessa tecnica — basta infondere il sapore nella panna calda prima di aggiungere la gelatina.",
    "img2_alt": "Panna cotta sformata nel piatto con salsa di fragole fresche e guarnizione di menta",
    "prose3_h2": "Preparazione in Anticipo e Servizio",
    "prose3": "La panna cotta è il dolce da preparare in anticipo per eccellenza. Si conserva in frigo fino a 3 giorni, coperta con pellicola. Puoi lasciarla negli stampini e aggiungere la salsa al momento di servire — non è necessario sformarla se la servi nei bicchieri. Anche la salsa di fragole si conserva per 3 giorni in frigo.",
    "faqs": [
      ("Perché la mia panna cotta non si è rassodata?", "O la gelatina non si è gonfiata correttamente (servono 5 minuti interi in acqua fredda), non si è sciolta completamente nella panna calda, o la panna non era abbastanza calda. Alcuni enzimi dell'ananas e del kiwi freschi degradano la gelatina — evita le versioni fresche di questi frutti nella salsa."),
      ("Posso usare il latte invece della panna?", "Puoi usare metà panna e metà latte intero per un risultato più leggero, ma la panna intera dà la caratteristica ricchezza. Non usare latte scremato — la panna cotta non si raddensarebbe bene e avrebbe un sapore acquoso."),
      ("Posso fare la panna cotta senza gelatina?", "Sì, usando l'agar-agar (un'alternativa vegetale). Usa metà della quantità indicata per la gelatina — l'agar rassofa più sodo, quindi 1¼ cucchiaino per questa ricetta. Scioglilo nella panna fredda prima di scaldarla, poi fai sobbollire per 2 minuti per attivarlo."),
      ("Come sformo la panna cotta in modo pulito?", "Passa un coltellino sottile lungo il bordo interno. Immergi il fondo dello stampino in acqua calda per 10 secondi. Metti un piatto sopra e capovolgi con decisione in un solo movimento rapido. Non esitare — l'esitazione causa rotture."),
      ("Qual è la migliore salsa per la panna cotta?", "Il coulis di fragole o frutti di bosco è il classico. La salsa al caramello salato è spettacolare. Una riduzione di aceto balsamico con fragole fresche è elegante e italiana. La salsa al caffè si abbina magnificamente alla panna cotta alla vaniglia. Quasi tutte le salse di frutta funzionano."),
    ],
  },

  # ─── 6 — arancini recipe ──────────────────────────────────
  {
    "slug": "arancini-recipe",
    "title": "Ricetta Arancini — Le Croccanti Polpette di Riso Siciliane Autentiche",
    "desc": "Autentici arancini siciliani: croccanti polpette di riso dorate ripiene di ragù di carne e mozzarella filante. Preparali a casa con questa ricetta completa passo-passo.",
    "tag": "Antipasti", "tag_color": "#e65100", "tag_bg": "#fff3e0",
    "h1": "Arancini Siciliani — Croccanti Polpette di Riso con Ragù e Mozzarella",
    "intro": "Gli arancini sono uno dei più grandi street food mai inventati. Croccanti, dorati, incredibilmente soddisfacenti — un guscio di risotto allo zafferano racchiude un cuore fuso di ragù di carne cotto lentamente e mozzarella filante. Questa è la ricetta siciliana autentica, preparata correttamente da zero.",
    "prep": "30 min", "cook": "1 ora", "total": "2 ore",
    "servings": "12 arancini", "calories": "~280", "difficulty": "Medio",
    "badge_text": "Classico Siciliano", "cuisine": "Italiana", "category": "Antipasti",
    "keywords": "ricetta arancini, arancini siciliani, polpette di riso, arancini di riso, come fare gli arancini",
    "cal_num": "280", "protein": "12g", "fat": "11g", "carbs": "34g",
    "ingredients": [
      "400g riso Arborio o Carnaroli",
      "1 litro di brodo di pollo o vegetale, caldo",
      "1 pizzico di fili di zafferano",
      "1 cipolla bianca, tritata finemente",
      "80g Parmigiano Reggiano, grattugiato",
      "30g burro",
      "— Per il ragù —",
      "200g carne macinata di manzo",
      "100g piselli surgelati",
      "1 barattolo (400g) di pomodori pelati tritati",
      "1 cipolla piccola · 1 spicchio d'aglio",
      "— Per la panatura e la frittura —",
      "200g mozzarella fresca, tagliata a cubetti piccoli",
      "3 uova, sbattute · 200g pangrattato",
      "Olio neutro per friggere in abbondanza",
    ],
    "steps": [
      "Prepara il ragù: soffriggi cipolla e aglio in olio d'oliva per 5 minuti. Aggiungi la carne, falla rosolare bene. Aggiungi pomodori tritati, piselli, sale e pepe. Fai sobbollire 25-30 minuti finché è denso. Fai raffreddare completamente.",
      "Prepara il risotto: soffriggi la cipolla nel burro finché è morbida. Aggiungi il riso, tostalo 2 minuti. Aggiungi il brodo con lo zafferano mestolo per mestolo, mescolando finché viene assorbito. Cuoci 18-20 minuti al dente. Incorpora il Parmigiano. Stendi su un vassoio e fai raffreddare completamente — minimo 1 ora.",
      "Forma gli arancini: bagnati le mani. Prendi una manciata di riso freddo (~70g), appiattiscila come un disco nel palmo. Metti 1 cucchiaio di ragù e 1-2 cubetti di mozzarella al centro. Chiudi il riso attorno al ripieno, dando forma decisa a una palla o un cono. Ripeti.",
      "Pana gli arancini: rotola ciascuno nell'uovo sbattuto, poi nel pangrattato. Premi bene affinché la panatura aderisca. Per una crosticina extra, fai una doppia panatura (uovo → pangrattato → uovo → pangrattato).",
      "Metti gli arancini panati in frigo per 30 minuti — questo li aiuta a mantenere la forma durante la frittura.",
      "Scalda l'olio a 175°C in una pentola profonda. Friggi 3-4 arancini alla volta per 3-4 minuti, girandoli delicatamente, finché sono dorati uniformemente. Non sovraffollare la pentola.",
      "Scola su carta assorbente. Aspetta 3-4 minuti prima di mangiare — l'interno deve raffreddarsi leggermente altrimenti ti scotti la bocca con il formaggio fuso.",
    ],
    "tips": [
      "Il risotto DEVE essere completamente freddo prima di formare gli arancini — il risotto caldo si sgretola.",
      "Le mani bagnate evitano che il riso si attacchi.",
      "La doppia panatura dà una crosticina più croccante e resistente.",
      "La temperatura dell'olio è fondamentale: troppo freddo = unto, troppo caldo = bruciato fuori e crudo dentro.",
    ],
    "prose1_h2": "Arancini: Palermo vs Catania — Il Dibattito sulla Forma",
    "prose1": "In Sicilia, gli arancini sono una cosa seria — e la forma è una questione di forte identità regionale. A Palermo, gli arancini sono rotondi (come le arance — 'arancini' significa 'arancette' in siciliano). A Catania e nella parte orientale dell'isola, sono a forma di cono, a rappresentare l'Etna. Entrambe le versioni contengono gli stessi ripieni, ma i catanesi saranno offesi se li fai rotondi. Se non sai da che parte stai, falli rotondi — è il classico.",
    "prose2_h2": "Posso Cuocerli al Forno invece di Friggerli?",
    "prose2": "Sì, ma il risultato è diverso. Gli arancini al forno hanno una crosticina più asciutta e meno dorata che non si sbriciola allo stesso modo soddisfacente. Se devi cuocerli al forno: spennellali con olio d'oliva e cuoci a 200°C per 25-30 minuti, girandoli a metà. Il risultato è comunque buono, ma se ti stai dando la pena di preparare gli arancini da zero, friggerli vale davvero la pena.",
    "img2_alt": "Arancino tagliato a metà che rivela la mozzarella fusa e il ripieno di ragù di carne",
    "prose3_h2": "Preparazione in Anticipo e Conservazione",
    "prose3": "Gli arancini si possono preparare in anticipo per fasi. Il ragù e il risotto si possono preparare 2 giorni prima. Gli arancini formati e panati si conservano in frigo per 24 ore prima di friggere. Gli arancini fritti si riscaldano bene in forno a 180°C per 10 minuti — recuperano quasi tutta la croccantezza.",
    "faqs": [
      ("Perché i miei arancini si sfaldano durante la frittura?", "Il risotto era ancora tiepido quando li hai formati, o non li hai pressati abbastanza saldamente. Anche il ripieno potrebbe essere troppo liquido — assicurati che il ragù sia denso, non acquoso. Il raffreddamento in frigo prima di friggere aiuta a mantenerli integri."),
      ("Posso congelare gli arancini?", "Sì — congelali dopo la panatura ma prima di friggerli. Congelali prima su un vassoio, poi trasferiscili in sacchetti. Friggili direttamente dal congelatore a 165°C per 5-6 minuti. Oppure congela già fritti, riscalda in forno a 180°C per 15-20 minuti."),
      ("Qual è il miglior riso per gli arancini?", "Arborio o Carnaroli — lo stesso riso ad alto contenuto di amido usato per il risotto. L'amido è ciò che rende il riso abbastanza appiccicoso da mantenere la forma. Non usare riso a grana lunga come il basmati."),
      ("Cosa posso usare come ripieno invece del ragù?", "Spinaci e ricotta è un ripieno vegetariano popolare. Prosciutto e mozzarella è un classico. Pistacchio e prosciutto è una specialità catanese. Burro e Parmigiano è il più semplice. Qualunque cosa usi deve essere fredda e non troppo umida."),
      ("Come capisco quando l'olio è abbastanza caldo?", "Usa un termometro per precisione (175°C). Senza: lascia cadere un po' di pangrattato — deve sfrigolare immediatamente e salire in superficie. Se affonda e rimane lì, l'olio è troppo freddo."),
    ],
  },

  # ─── 7 — pasta amatriciana ────────────────────────────────
  {
    "slug": "pasta-amatriciana-recipe",
    "title": "Ricetta Pasta all'Amatriciana Autentica — Il Classico Romano Originale",
    "desc": "La vera Amatriciana: guanciale, pomodori San Marzano, Pecorino Romano — niente cipolla, niente aglio, niente scorciatoie. La ricetta ufficiale di Amatrice, Italia.",
    "tag": "Pasta", "tag_color": "#1565c0", "tag_bg": "#e3f2fd",
    "h1": "Pasta all'Amatriciana Autentica — La Ricetta Ufficiale di Amatrice",
    "intro": "La pasta all'Amatriciana è uno dei quattro piatti di pasta canonici di Roma — e uno dei più fraintesi. Niente cipolla. Niente aglio. Niente olio d'oliva. Solo guanciale reso nel proprio grasso, vino bianco secco, pomodori San Marzano e Pecorino Romano. Questa è la ricetta ufficiale registrata dal Comune di Amatrice.",
    "prep": "5 min", "cook": "20 min", "total": "25 min",
    "servings": "4 porzioni", "calories": "~520", "difficulty": "Facile",
    "badge_text": "25 Min", "cuisine": "Italiana", "category": "Pasta",
    "keywords": "pasta amatriciana, ricetta amatriciana, amatriciana autentica, bucatini amatriciana, ricetta romana",
    "cal_num": "520", "protein": "20g", "fat": "18g", "carbs": "70g",
    "ingredients": [
      "400g bucatini o rigatoni",
      "150g guanciale, tagliato a listarelle",
      "400g pomodori San Marzano (in scatola, interi)",
      "100g Pecorino Romano DOP, grattugiato finemente",
      "100ml vino bianco secco",
      "1 peperoncino secco",
      "Sale per l'acqua della pasta",
    ],
    "steps": [
      "Metti le listarelle di guanciale in una padella FREDDA — senza olio. Cuoci a fuoco medio per 8-10 minuti, mescolando di tanto in tanto, finché il grasso si scioglie e il guanciale è croccante e dorato.",
      "Aggiungi il peperoncino e il vino bianco. Lascia sfrigolare e ridurre completamente — circa 2 minuti. L'alcol deve evaporare completamente.",
      "Rimuovi metà delle listarelle di guanciale e mettile da parte (torneranno alla fine per la consistenza).",
      "Schiaccia i pomodori San Marzano a mano e aggiungili alla padella con il grasso del guanciale. Aggiusta leggermente di sale. Fai sobbollire 15 minuti a fuoco medio finché la salsa si addensa leggermente.",
      "Nel frattempo cuoci i bucatini in acqua ben salata fino al dente. Conserva 1 tazza di acqua di cottura prima di scolare.",
      "Aggiungi la pasta scolata alla salsa. Mescola vigorosamente a fuoco medio per 1-2 minuti, aggiungendo acqua di cottura se necessario per raggiungere una consistenza lucida.",
      "Togli dal fuoco. Aggiungi metà del Pecorino e mescola. Impiatta, guarnisci con il guanciale croccante tenuto da parte e il Pecorino rimanente. Servi immediatamente.",
    ],
    "tips": [
      "Inizia il guanciale in una padella fredda — questo rende il grasso correttamente senza bruciare l'esterno.",
      "Mai l'olio d'oliva — il guanciale fornisce tutto il grasso necessario al piatto.",
      "La pasta ufficiale è il bucatino (spaghetto spesso e cavo). Il rigatone è l'alternativa accettabile.",
      "Non aggiungere mai aglio o cipolla — non sono nella ricetta originale.",
    ],
    "prose1_h2": "La Ricetta Ufficiale: Cosa è Autentico e Cosa Non lo è",
    "prose1": "Il paese di Amatrice, tra i monti del Lazio, ha registrato la propria ricetta ufficiale dell'amatriciana nel 2015. Gli ingredienti sono non negoziabili: guanciale (non pancetta, non bacon), pomodori San Marzano, Pecorino Romano, vino bianco e peperoncino. Niente olio d'oliva — il grasso del guanciale è il mezzo di cottura. Niente cipolla, niente aglio — aggiunte che compaiono in innumerevoli ricette di 'amatriciana' online ma che non hanno posto nel piatto autentico.",
    "prose2_h2": "Guanciale vs Pancetta: La Differenza è Davvero Così Grande?",
    "prose2": "Sì. Il guanciale (guancia di maiale stagionata) ha un contenuto di grasso significativamente più elevato e un sapore di maiale più intenso e leggermente dolce rispetto alla pancetta (pancia di maiale stagionata). Quando viene reso, il grasso del guanciale ha una qualità più setosa e aromatica che cambia fondamentalmente il carattere del piatto. Ad Amatrice, usare la pancetta è considerata una sostituzione inaccettabile. Fuori dall'Italia, il guanciale si trova in gastronomie italiane e negozi specializzati — vale la pena cercarlo.",
    "img2_alt": "Bucatini all'amatriciana con guanciale croccante e Pecorino Romano in una ciotola scura",
    "prose3_h2": "Conservazione e Riscaldamento",
    "prose3": "La salsa amatriciana si conserva in frigo per 3 giorni e si congela bene per 3 mesi. Riscalda con un goccio d'acqua. Cuoci la pasta fresca ogni volta — la pasta cotta nella salsa troppo a lungo diventa molle. Mescola la salsa riscaldata con pasta appena cotta e aggiungi il Pecorino alla fine.",
    "faqs": [
      ("Perché non c'è cipolla nell'amatriciana autentica?", "La ricetta originale di Amatrice esclude esplicitamente la cipolla. La ricetta ufficiale del Comune elenca esattamente 7 ingredienti senza variazioni. Aggiungere la cipolla è un compromesso romano diventato comune nelle trattorie, ma non è amatriciana autentica — è una versione semplificata."),
      ("Che vino uso nell'amatriciana?", "Un vino bianco secco — Verdicchio, Pinot Grigio, o qualsiasi bianco secco neutro. Il vino serve per sfumare e aggiungere acidità, non sapore. Deve evaporare completamente prima di aggiungere i pomodori."),
      ("Posso usare la pancetta invece del guanciale?", "Puoi usare la pancetta all'occorrenza. Non usare il bacon affumicato — l'affumicato stride con il piatto. Vale la pena trovare il guanciale autentico in una buona gastronomia italiana."),
      ("Qual è la pasta corretta per l'amatriciana?", "Il bucatino è tradizionale — uno spaghetto spesso e cavo che trattiene la salsa all'interno. Il rigatone è la seconda scelta. Gli spaghetti funzionano ma sono meno autentici. Non usare mai pasta corta come le penne."),
      ("L'amatriciana è piccante?", "Tradizionalmente sì — un peperoncino secco dà al piatto un calore di fondo presente ma non preponderante. Se vuoi più piccante, aggiungi un pizzico di peperoncino in scaglie. Se non vuoi niente di piccante, ometti il peperoncino del tutto."),
    ],
  },

  # ─── 8 — chicken piccata ──────────────────────────────────
  {
    "slug": "chicken-piccata-recipe",
    "title": "Ricetta Pollo alla Piccata — Salsa al Limone e Capperi in 25 Minuti",
    "desc": "Il classico pollo alla piccata con una salsa brillante di burro, limone e capperi. Tenere fettine di pollo dorate in padella, con una salsa da ristorante, pronta in 25 minuti.",
    "tag": "Secondi", "tag_color": "#2e7d32", "tag_bg": "#e8f5e9",
    "h1": "Pollo alla Piccata — Salsa al Burro, Limone e Capperi in 25 Minuti",
    "intro": "Il pollo alla piccata è il piatto italo-americano che tutti dovrebbero avere nella propria rotazione settimanale. Fettine sottili infarinate, dorate in padella, poi finite in una brillante salsa al burro, limone e capperi che si prepara in pochi minuti. Qualità da ristorante, fatica da cucina casalinga.",
    "prep": "10 min", "cook": "15 min", "total": "25 min",
    "servings": "4 porzioni", "calories": "~420", "difficulty": "Facile",
    "badge_text": "25 Min", "cuisine": "Italo-Americana", "category": "Secondi",
    "keywords": "ricetta pollo piccata, pollo alla piccata, pollo al limone e capperi, secondo di pollo veloce, pollo piccata facile",
    "cal_num": "420", "protein": "38g", "fat": "22g", "carbs": "12g",
    "ingredients": [
      "4 petti di pollo disossati e senza pelle (circa 170g ciascuno)",
      "60g farina 00",
      "Sale e pepe nero macinato fresco",
      "4 cucchiai di burro non salato, divisi",
      "3 cucchiai di olio extravergine d'oliva",
      "4 spicchi d'aglio, tritati",
      "120ml vino bianco secco o brodo di pollo",
      "120ml succo di limone fresco (circa 3 limoni)",
      "60ml brodo di pollo",
      "3 cucchiai di capperi, scolati e sciacquati",
      "3 cucchiai di prezzemolo a foglia piatta fresco, tritato",
      "Fette di limone per servire",
    ],
    "steps": [
      "Batti i petti di pollo a uno spessore uniforme di 1,2 cm tra due fogli di pellicola. Condisci generosamente con sale e pepe su entrambi i lati.",
      "Infarina ogni fettina, scuotendo l'eccesso. Non pressare la farina — basta una leggera copertura.",
      "Scalda 2 cucchiai di burro e l'olio d'oliva in una padella grande a fuoco medio-alto finché il burro fa la schiuma. Aggiungi le fettine di pollo senza sovrapporle. Cuoci 3-4 minuti per lato finché sono dorate e ben cotte. Togli e copri con un foglio di alluminio.",
      "Nella stessa padella, soffriggi l'aglio per 30 secondi a fuoco medio.",
      "Aggiungi il vino bianco e lascia ridurre per 1 minuto, raschiando tutti i pezzi dorati — aggiungono un sapore enorme.",
      "Aggiungi il succo di limone, il brodo di pollo e i capperi. Porta a sobbollire e cuoci 2-3 minuti finché si riduce leggermente.",
      "Togli dal fuoco. Aggiungi a spirale i restanti 2 cucchiai di burro freddo per emulsionare la salsa — questo è ciò che la rende lucida e ricca.",
      "Rimetti il pollo nella padella, versaci la salsa sopra. Guarnisci con il prezzemolo fresco e le fette di limone. Servi immediatamente.",
    ],
    "tips": [
      "Battere il pollo è indispensabile — spessore irregolare significa cottura irregolare.",
      "Non saltare la farina — aiuta il pollo a dorarsi e addensa leggermente la salsa.",
      "Incorpora il burro freddo FUORI dal fuoco — questa tecnica rende la salsa setosa e lucida.",
      "Solo succo di limone fresco — quello in bottiglia ha un sapore piatto e acidulo.",
    ],
    "prose1_h2": "Le Origini Italiane della Piccata",
    "prose1": "La piccata è in realtà una tecnica di cottura italiana, non solo un piatto. 'Piccata' descrive carne o pesce tagliati sottili, infarinati e cotti nel burro con limone e vino. In Italia, il vitello piccata è l'originale — il pollo alla piccata è l'adattamento italo-americano che è diventato un piatto fisso dei ristoranti italiani negli Stati Uniti. La tecnica è la stessa, cambia solo la proteina.",
    "prose2_h2": "Cosa Servire con il Pollo alla Piccata",
    "prose2": "La brillante salsa al limone e capperi si abbina meglio a contorni semplici e amidacei che possono assorbirla. Il capellino d'angelo condito con olio d'oliva è l'accompagnamento classico. Il purè di patate si abbina magnificamente. Gli asparagi o i broccoli saltati aggiungono una nota verde. Evita contorni pesanti e cremosi che competono con la brillantezza della salsa. Una semplice insalata verde condita con olio d'oliva è tutto quello che serve per completare il pasto.",
    "img2_alt": "Fettine di pollo alla piccata nella salsa al burro, limone e capperi con prezzemolo fresco e fette di limone",
    "prose3_h2": "Conservazione e Riscaldamento",
    "prose3": "Il pollo alla piccata si conserva in frigo per 3 giorni in un contenitore ermetico. Riscalda delicatamente in padella a fuoco basso con un goccio di brodo per sciogliere la salsa. Evita il microonde — il pollo diventa gommoso e la salsa si separa.",
    "faqs": [
      ("Che vino usare per il pollo alla piccata?", "Un vino bianco secco con buona acidità — Pinot Grigio, Sauvignon Blanc o Chardonnay vanno tutti bene. Evita i vini dolci. Se preferisci non usare il vino, sostituisci con brodo di pollo e aggiungi una spremitura extra di limone."),
      ("Posso fare il pollo alla piccata senza capperi?", "Sì — il piatto sarà meno sapido ma comunque delizioso. Alcune ricette sostituiscono le olive verdi tagliate sottili. Altre aggiungono un cucchiaio di senape di Digione per profondità senza il sapore dei capperi."),
      ("Come capisco quando il pollo è ben cotto?", "La temperatura interna deve raggiungere 74°C. Visivamente, i succhi devono essere chiari quando punzi la parte più spessa. A 1,2 cm di spessore, 3-4 minuti per lato a fuoco medio-alto è affidabile."),
      ("Perché la mia salsa è unta invece di setosa?", "Il burro è stato aggiunto a una salsa troppo calda, o non l'hai incorporato correttamente. Togli prima la padella dal fuoco, poi aggiungi il burro freddo a spirale finché si emulsiona. Se si rompe, la salsa è troppo calda."),
      ("Posso usare le cosce di pollo invece dei petti?", "Sì — le cosce disossate e senza pelle funzionano benissimo e sono più indulgenti dei petti. Appiattiscile, cuocile leggermente di più (5 minuti per lato), e il risultato è spesso più saporito per il più alto contenuto di grasso."),
    ],
  },

  # ─── 9 — Italian wedding soup ─────────────────────────────
  {
    "slug": "italian-wedding-soup-recipe",
    "title": "Ricetta Minestra Maritata — La Vera Zuppa Italiana di Polpettine e Verdure",
    "desc": "La vera minestra maritata: piccole polpettine fatte in casa, scarola o spinaci e pasta in un ricco brodo di pollo. Il comfort food italiano per eccellenza — per tutta la famiglia.",
    "tag": "Zuppe", "tag_color": "#00695c", "tag_bg": "#e0f2f1",
    "h1": "Minestra Maritata — Polpettine Fatte in Casa, Brodo Ricco, Comfort Food Perfetto",
    "intro": "La minestra maritata non ha niente a che fare con i matrimoni. 'Minestra maritata' significa 'zuppa sposata' — un riferimento al perfetto connubio tra carne e verdure in un brodo ricco e caldo. Questa versione dal gusto unico con piccole polpettine fatte in casa è il tipo di ricetta che sfama tutta la famiglia e ha un sapore ancora migliore il giorno dopo.",
    "prep": "30 min", "cook": "30 min", "total": "1 ora",
    "servings": "6-8 porzioni", "calories": "~340", "difficulty": "Facile",
    "badge_text": "Comfort Food", "cuisine": "Italo-Americana", "category": "Zuppe",
    "keywords": "ricetta minestra maritata, zuppa di polpettine italiana, minestra maritata napoletana, zuppa italiana, polpettine in brodo",
    "cal_num": "340", "protein": "24g", "fat": "14g", "carbs": "28g",
    "ingredients": [
      "— Per le polpettine —",
      "450g carne macinata di manzo (o metà manzo e metà maiale)",
      "50g pangrattato",
      "1 uovo",
      "30g Parmigiano Reggiano, grattugiato",
      "2 spicchi d'aglio, tritati",
      "2 cucchiai di prezzemolo fresco, tritato",
      "Sale, pepe ed erbe aromatiche italiane",
      "— Per la zuppa —",
      "2 litri di brodo di pollo di buona qualità",
      "200g pasta piccola (acini di pepe, ditalini o orzo)",
      "200g spinacini o scarola, grossolanamente tritati",
      "2 carote, a dadini · 2 gambi di sedano, a dadini",
      "1 cipolla, a dadini",
      "Crosta di Parmigiano Reggiano (facoltativo ma straordinario)",
      "Sale, pepe, Parmigiano extra per servire",
    ],
    "steps": [
      "Prepara le polpettine: unisci tutti gli ingredienti per le polpettine in una ciotola e mescola delicatamente. Forma delle palline minuscole — circa delle dimensioni di una biglia (diametro 1-1,5 cm). Disponi su una teglia rivestita di carta da forno.",
      "Cuoci le polpettine a 200°C per 12-15 minuti finché sono dorate e ben cotte. La cottura al forno le mantiene tenere ed evita di aggiungere grasso extra al brodo.",
      "Mentre le polpettine cuociono, soffriggi cipolla, carote e sedano a dadini in olio d'oliva in una pentola grande a fuoco medio per 8 minuti finché si ammorbidiscono.",
      "Aggiungi il brodo di pollo e la crosta di Parmigiano se la usi. Porta a sobbollire. La crosta aggiunge una profondità di sapore incredibile — non saltarla se ne hai una.",
      "Aggiungi le polpettine cotte al forno al brodo sobbollente. Fai sobbollire 10 minuti.",
      "Aggiungi la pasta e cuoci secondo le istruzioni del pacchetto meno 2 minuti — continuerà a cuocere nel calore residuo.",
      "Aggiungi gli spinaci o la scarola. Mescola e fai sobbollire 2 minuti finché appassiscono. Rimuovi la crosta di Parmigiano.",
      "Assaggia e aggiusta il condimento. Versa nei piatti fondi e servi con Parmigiano extra grattugiato e pane italiano croccante.",
    ],
    "tips": [
      "Cuoci le polpettine al forno, non friggerle — restano tenere e il brodo rimane pulito.",
      "Aggiungi una crosta di Parmigiano al brodo — dona una profondità umami incredibile.",
      "Se prepari in anticipo, cuoci la pasta separatamente — assorbe troppo liquido se rimane nella zuppa.",
      "La zuppa è sempre migliore il giorno dopo quando i sapori si sono amalgamati.",
    ],
    "prose1_h2": "Il Nome Non Ha Niente a che Fare con i Matrimoni",
    "prose1": "Uno dei miti alimentari più persistenti è che la minestra maritata venga servita ai matrimoni. Non è così. Il nome viene dal piatto napoletano 'minestra maritata' — letteralmente 'zuppa sposata' — che si riferisce all'armonioso connubio tra carne e verdure in un brodo ricco. La versione italo-americana ha evoluto questo classico nella zuppa di polpettine e verdure che conosciamo oggi. A Napoli, l'originale include una gamma molto più ampia di carni e verdure, cotte lentamente in un brodo dal sapore profondo.",
    "prose2_h2": "Scarola vs Spinaci: Quale è Meglio?",
    "prose2": "La scarola (una verdura a foglia leggermente amara) è la scelta tradizionale — la sua leggera amarezza bilancia la ricchezza delle polpettine e del brodo. Gli spinacini sono il sostituto più comune — più delicati, più facilmente reperibili, e ugualmente deliziosi. Il cavolo riccio funziona bene per una consistenza più sostanziosa. Qualunque cosa scegli, aggiungila negli ultimi 2 minuti di cottura — appassisce rapidamente e perde il suo colore vivace se cuoce troppo.",
    "img2_alt": "Ciotola di minestra maritata con piccole polpettine, spinaci e pasta in brodo dorato",
    "prose3_h2": "Conservazione e Congelamento",
    "prose3": "Conserva la zuppa senza pasta per i migliori risultati — la pasta assorbe liquido e diventa molle. Conserva in frigo fino a 4 giorni. Congela la zuppa (senza pasta) per un massimo di 3 mesi. Cuoci la pasta fresca quando riscaldi e aggiungila alla zuppa calda. Le polpettine si congelano magnificamente — fai una doppia quantità e congela metà per la prossima volta.",
    "faqs": [
      ("Che pasta si usa nella minestra maritata?", "Gli acini di pepe (pasta a forma di piccole perle) sono tradizionali. I ditalini (tubetti piccoli), l'orzo o le stelline funzionano tutti bene. La pasta deve essere abbastanza piccola da stare in un cucchiaio con una polpettina — la pasta grande sovrasta la zuppa."),
      ("Posso usare il brodo pronto?", "Sì, ma la qualità conta enormemente in una zuppa a base di brodo. Usa un buon brodo di pollo di qualità, a basso contenuto di sodio, e aggiungi la crosta di Parmigiano — trasformerà anche un brodo mediocre. Il brodo di pollo fatto in casa è spettacolare se ce l'hai."),
      ("Come faccio a mantenere rotonde le polpettine?", "Tieni le mani bagnate durante la lavorazione — le mani asciutte causano appiccicosità e deformazione. Lavora delicatamente e velocemente. Anche mettere il composto di carne in frigo per 15 minuti prima di formare le palline aiuta."),
      ("La minestra maritata è uguale alla minestrone?", "No. Il minestrone è una zuppa di verdure densa con pomodori e legumi. La minestra maritata è una zuppa a base di brodo limpido incentrata sull'interazione tra carne (polpettine) e verdure. I profili di sapore sono completamente diversi."),
      ("Posso rendere questa zuppa vegetariana?", "Sì — usa brodo vegetale, sostituisci le polpettine con tortellini piccoli o fagioli cannellini, e aggiungi verdure extra come zucchine e cavolo riccio. Aggiungi un cucchiaio di miso bianco al brodo per profondità."),
    ],
  },

  # ─── 10 — homemade gnocchi ────────────────────────────────
  {
    "slug": "homemade-gnocchi-recipe",
    "title": "Ricetta Gnocchi di Patate Fatti in Casa — Leggeri, Soffici, Perfetti Ogni Volta",
    "desc": "Impara a fare gli gnocchi di patate dal gusto unico: leggeri, soffici e dalla consistenza perfetta. La tecnica della nonna italiana che fa tutta la differenza.",
    "tag": "Pasta", "tag_color": "#1565c0", "tag_bg": "#e3f2fd",
    "h1": "Gnocchi di Patate Fatti in Casa — Leggeri, Soffici, alla Maniera della Nonna",
    "intro": "Gli gnocchi di patate fatti in casa sono una delle cose più soddisfacenti che puoi preparare da zero — e una delle più fraintese. La differenza tra gnocchi pesanti e densi e gnocchi leggeri e soffici dipende da tre cose: la giusta patata, il giusto rapporto di farina e la mano più leggera possibile nel lavorare l'impasto.",
    "prep": "30 min", "cook": "30 min", "total": "1 ora",
    "servings": "4 porzioni", "calories": "~380", "difficulty": "Medio",
    "badge_text": "Dal Gusto Unico", "cuisine": "Italiana", "category": "Pasta",
    "keywords": "ricetta gnocchi di patate, gnocchi fatti in casa, come fare gli gnocchi, gnocchi soffici, gnocchi della nonna",
    "cal_num": "380", "protein": "10g", "fat": "4g", "carbs": "76g",
    "ingredients": [
      "1 kg di patate farinose (a pasta bianca — NON patate cerose)",
      "150-180g farina 00, più extra per spolverare",
      "1 tuorlo d'uovo grande",
      "1 cucchiaino di sale fino marino",
      "Un pizzico di noce moscata (facoltativo ma consigliato)",
    ],
    "steps": [
      "Cuoci le patate intere al forno: punzecchiale con una forchetta e cuocile a 200°C per 1 ora finché sono completamente tenere. NON bollirle — le patate bollite assorbono acqua e producono gnocchi pesanti.",
      "Mentre sono ancora calde, tagliale e raschia la polpa. Passala immediatamente nello schiacciapatate su una superficie pulita. Stendila per far uscire il vapore per 5 minuti.",
      "Fai un buco al centro. Aggiungi il tuorlo, il sale, la noce moscata e 150g di farina. Usa una forchetta per incorporare, poi usa le mani nel modo più leggero possibile.",
      "Impasta DELICATAMENTE per 30-60 secondi — giusto finché l'impasto si compatta. Deve essere morbido e leggermente appiccicoso. Resisti all'impulso di aggiungere altra farina — questa è la chiave per gnocchi leggeri.",
      "Dividi l'impasto in 6 porzioni. Rotola ciascuna in un salsicciotto di circa 2 cm di diametro su una superficie leggermente infarinata. Taglia a pezzi da 2 cm.",
      "Facoltativo ma consigliato: rotola ogni pezzo su una forchetta o su un riga-gnocchi per creare le righe — queste trattengono la salsa.",
      "Cuoci immediatamente OPPURE conserva in frigo su un vassoio infarinato per un massimo di 2 ore. Per cuocere: immergi in acqua salata in ebollizione. Sono pronti quando salgono in superficie più 30 secondi extra. Rimuovi con una schiumarola.",
      "Condisci immediatamente con la tua salsa — burro nocciola e salvia, crema al gorgonzola o classico pomodoro. Servi subito.",
    ],
    "tips": [
      "Cuoci al forno, non bollire le patate — il contenuto d'acqua è il nemico degli gnocchi leggeri.",
      "Usa lo schiacciapatate — mai il robot da cucina, che fa la colla.",
      "Aggiungi la farina gradualmente e fermati appena l'impasto tiene insieme.",
      "Lavora velocemente mentre la patata è ancora calda — incorpora meglio la farina.",
    ],
    "prose1_h2": "Perché Cuocere le Patate al Forno Fa Tutta la Differenza",
    "prose1": "La maggior parte delle ricette di gnocchi dice di bollire le patate. È un errore che le nonne italiane non farebbero mai. La bollitura introduce acqua nella patata, che poi devi compensare con più farina — rendendo gli gnocchi densi e gommosi. La cottura al forno asciuga la patata dall'interno, dandoti una polpa amidacea e soffice che richiede la minima quantità di farina per legarsi. Meno farina aggiungi, più leggeri saranno gli gnocchi finali.",
    "prose2_h2": "I Migliori Condimenti per gli Gnocchi Fatti in Casa",
    "prose2": "Il burro nocciola e salvia (burro e salvia) è il classico e il migliore — il burro noisette e la salvia profumata lasciano brillare gli gnocchi di patate. La salsa al gorgonzola cremosa riveste magnificamente e aggiunge ricchezza. Il semplice pomodoro e basilico è sempre giusto. Il pesto genovese è un abbinamento tradizionale. Evita sughi di carne molto corposi e pesanti — i delicati gnocchi non reggono il confronto. Il condimento deve rivestire e complementare, non sopraffare.",
    "img2_alt": "Gnocchi di patate fatti in casa nel burro nocciola e salvia con scaglie di Parmigiano",
    "prose3_h2": "Congelamento e Conservazione",
    "prose3": "Gli gnocchi crudi si congelano magnificamente. Disponili su un vassoio infarinato e congela finché sono sodi (1 ora), poi trasferiscili nei sacchetti da freezer. Cuocili direttamente dal congelato in acqua salata in ebollizione — impiegano circa 1 minuto in più. Gli gnocchi cotti non si conservano bene — diventano appiccicosi e molli. Prepara e cuoci sempre gli gnocchi lo stesso giorno, oppure congelali crudi.",
    "faqs": [
      ("Perché i miei gnocchi sono densi e pesanti?", "Quasi sempre causato da troppa umidità nella patata (dalla bollitura) o troppa farina. Cuoci le patate al forno, aggiungi la minor quantità di farina possibile, e lavora l'impasto con una mano leggerissima. Lavorare troppo sviluppa il glutine, che rende gli gnocchi duri."),
      ("Quali patate sono migliori per gli gnocchi?", "Patate farinose e amidacee: a pasta bianca, Russet o King Edward. Evita le patate cerose — non si schiacciano bene e producono gnocchi collosi."),
      ("Posso fare gli gnocchi senza uovo?", "Sì — i tradizionali gnocchi veneti non hanno uovo. Sono leggermente più delicati e fragili, ma leggeri e deliziosi. Ometti il tuorlo e aggiungi la minima farina necessaria."),
      ("Come capisco quando gli gnocchi sono cotti?", "Salgono in superficie quando sono cotti. Aspetta che salgano, poi dagli altri 30 secondi prima di rimuoverli con una schiumarola. Non bollirli per un tempo prestabilito — il galleggiamento è l'unico indicatore affidabile."),
      ("Devo fare le righe sugli gnocchi?", "Le righe sono facoltative ma servono a uno scopo: trattengono meglio la salsa rispetto agli gnocchi lisci. Rotola ogni pezzo sul dorso di una forchetta o su un riga-gnocchi. Vale i 5 minuti extra per preparazioni con salsa abbondante."),
    ],
  },

  # ─── 11 — focaccia recipe ─────────────────────────────────
  {
    "slug": "italian-focaccia-recipe",
    "title": "Ricetta Focaccia Italiana — Morbida, Croccante, Autentica Focaccia Genovese",
    "desc": "L'autentica focaccia ligure: incredibilmente morbida all'interno, croccante sotto, con le fossette colme di olio extravergine e sale marino in scaglie. Si cuoce in una teglia, senza impastatrice.",
    "tag": "Lievitati", "tag_color": "#e65100", "tag_bg": "#fff3e0",
    "h1": "Ricetta Focaccia Italiana — L'Autentica Focaccia Genovese Ligure",
    "intro": "La vera focaccia italiana — la focaccia genovese della Liguria — non assomiglia per niente al pane spesso e secco che si trova nella maggior parte dei forni. Ha le fossette colme di olio extravergine d'oliva, è croccante sotto dove l'olio ha dorato la teglia, incredibilmente morbida e soffice all'interno, e rifinita con sale marino grosso. Questa ricetta la centra perfettamente.",
    "prep": "20 min", "cook": "25 min", "total": "2 ore e 30 min",
    "servings": "12 pezzi", "calories": "~220", "difficulty": "Facile",
    "badge_text": "Senza Impastatrice", "cuisine": "Italiana", "category": "Lievitati",
    "keywords": "ricetta focaccia, focaccia italiana, focaccia genovese, focaccia fatta in casa, pane focaccia facile",
    "cal_num": "220", "protein": "5g", "fat": "8g", "carbs": "34g",
    "ingredients": [
      "500g (4 tazze) farina di forza o farina 00",
      "7g (1 bustina) lievito di birra secco istantaneo",
      "350ml (1½ tazze) acqua tiepida",
      "10g (2 cucchiaini) sale fino",
      "10g (2 cucchiaini) zucchero",
      "— Per la salamoia —",
      "80ml (⅓ tazza) olio extravergine d'oliva, diviso",
      "80ml (⅓ tazza) acqua calda",
      "1 cucchiaino di sale fino",
      "— Condimenti —",
      "Sale marino in scaglie (Maldon o fleur de sel)",
      "Rosmarino fresco (facoltativo)",
    ],
    "steps": [
      "Mescola farina, lievito, zucchero e sale in una ciotola capiente. Aggiungi 4 cucchiai di olio extravergine e l'acqua tiepida. Mescola con una forchetta finché si forma un impasto grezzo e appiccicoso. Non serve impastare.",
      "Copri la ciotola e lascia lievitare a temperatura ambiente per 1 ora, finché raddoppia. L'impasto deve essere molto umido e pieno di bollicine.",
      "Versa 3 cucchiai di olio extravergine in una teglia da 33x23cm. Trasferisci l'impasto nella teglia. Non sgonfiarlo — usa le dita unte per stenderlo delicatamente verso i bordi. Non arriverà ai bordi subito, è normale.",
      "Lascia riposare 20 minuti. Stendi di nuovo verso i bordi con delicatezza. Copri e lascia lievitare altri 30-45 minuti finché è ben gonfio.",
      "Prepara la salamoia: emulsiona con una frusta 80ml di olio extravergine + 80ml di acqua calda + 1 cucchiaino di sale.",
      "Versa la salamoia su tutta la superficie dell'impasto. Premi con le dita per formare delle fossette profonde su tutta la superficie — non essere timido, vai in profondità. La salamoia si raccoglierà nelle fossette — è perfetto così.",
      "Cospargi generosamente di sale in scaglie e rosmarino se lo usi. Lascia riposare 10 minuti.",
      "Inforna a 230°C per 20-25 minuti finché è dorata in superficie e molto croccante sotto. Il fondo deve risultare dorato e croccante quando sollevi un angolo.",
    ],
    "tips": [
      "Più l'impasto è umido, più la focaccia sarà morbida — resisti alla tentazione di aggiungere altra farina.",
      "La salamoia (olio + acqua + sale) è il segreto della texture autentica ligure.",
      "Non essere delicato con le fossette — premi fino in fondo con le dita.",
      "Controlla il fondo, non la superficie — il fondo deve essere dorato e croccante.",
    ],
    "prose1_h2": "Il Segreto: La Salamoia",
    "prose1": "La maggior parte delle ricette di focaccia si limita a irrorare con olio in superficie. L'autentica focaccia genovese usa invece la salamoia — un'emulsione vigorosa di olio extravergine, acqua e sale sbattuti insieme. Quando questa salamoia viene versata sull'impasto e spinta nelle fossette, crea due cose: le pozze di olio che rendono croccante la superficie, e il vapore che mantiene l'interno incredibilmente umido. Questo è il passaggio che distingue la vera focaccia ligure da tutto il resto.",
    "prose2_h2": "Varianti di Condimento",
    "prose2": "La focaccia ligure classica si serve liscia con solo sale in scaglie — il sapore dell'impasto e dell'olio extravergine basta e avanza. Ma la focaccia è infinitamente versatile: cipolle rosse a fette e olive (focaccia barese), pomodorini e origano (focaccia pugliese), rosmarino e sale grosso (la versione più diffusa), oppure cipolle caramellate e salvia fresca. I formaggi — mozzarella, taleggio — possono essere aggiunti negli ultimi 5 minuti di cottura.",
    "img2_alt": "Primo piano di focaccia dorata con fossette croccanti colme di olio extravergine e sale in scaglie",
    "prose3_h2": "Conservazione e Riscaldamento",
    "prose3": "La focaccia è migliore il giorno stesso della cottura. Conserva gli avanzi a temperatura ambiente in un sacchetto di carta per 1-2 giorni — mai in frigorifero, che la indurisce. Per riscaldarla: metti in forno caldo (200°C) per 5 minuti o in una padella calda finché il fondo torna croccante. La focaccia si congela bene — taglia a fette, congela, e tosta direttamente da congelata.",
    "faqs": [
      ("Perché la mia focaccia viene densa?", "L'impasto non ha lievitato abbastanza, il lievito era scaduto (controlla la data), oppure hai aggiunto troppa farina. L'impasto della focaccia deve essere molto umido e appiccicoso — se riesci a lavorarlo con le mani, probabilmente ha troppa farina."),
      ("Come ottengo il fondo croccante?", "È essenziale abbondante olio extravergine nella teglia — circa 3-4 cucchiai. L'olio deve ricoprire visibilmente il fondo della teglia. Cuoci ad alta temperatura (230°C) e controlla il fondo sollevando un angolo dopo 20 minuti."),
      ("Posso preparare la focaccia la sera prima?", "Sì — la lievitazione lenta in frigorifero migliora notevolmente il sapore. Dopo l'impasto, copri e metti in frigorifero per tutta la notte (fino a 18 ore). Il giorno dopo, porta a temperatura ambiente per 1 ora prima di stendere e infornare. Il sapore sarà molto più complesso."),
      ("Che farina devo usare?", "La farina di forza dà la migliore consistenza e croccantezza. La farina 00 italiana produce una focaccia più morbida e delicata. La farina 0 comune funziona se non hai altro. Evita la farina integrale in questa ricetta — rende la focaccia densa."),
      ("Posso usare lievito di birra fresco invece di quello secco?", "Sì — scioglilo nell'acqua tiepida con lo zucchero e aspetta 5-10 minuti finché fa la schiuma. Poi procedi con la ricetta come indicato. Usa circa 20g di lievito fresco al posto della bustina da 7g di lievito secco."),
    ],
  },

  # ─── 12 — semifreddo recipe ───────────────────────────────
  {
    "slug": "semifreddo-recipe",
    "title": "Ricetta Semifreddo — Il Dolce Gelato Italiano Senza Gelatiera",
    "desc": "Il semifreddo italiano: cremoso, gelato, a metà strada tra gelato e mousse. Nessuna gelatiera necessaria. Preparalo la sera prima e stupisci ogni ospite.",
    "tag": "Dolci", "tag_color": "#6a1b9a", "tag_bg": "#f3e5f5",
    "h1": "Ricetta Semifreddo — Dolce Gelato Italiano Senza Gelatiera",
    "intro": "Semifreddo — 'mezzo freddo' in italiano — è il dessert gelato che nessun ristorante italiano si può permettere di non avere in carta. È più cremoso del gelato, più leggero della mousse, e non richiede una gelatiera. Preparalo la sera prima, affettalo a tavola e guarda tutti ammutolire.",
    "prep": "25 min", "cook": "0 min", "total": "6 ore (congelamento)",
    "servings": "8 porzioni", "calories": "~380", "difficulty": "Medio",
    "badge_text": "Senza Gelatiera", "cuisine": "Italiana", "category": "Dolci",
    "keywords": "ricetta semifreddo, semifreddo italiano, gelato senza gelatiera, semifreddo senza gelatiera, dolce gelato italiano",
    "cal_num": "380", "protein": "7g", "fat": "26g", "carbs": "32g",
    "ingredients": [
      "4 uova grandi, separate",
      "150g (¾ tazza) zucchero semolato fine, diviso",
      "400ml (1⅔ tazze) panna fresca da montare, fredda",
      "2 cucchiaini di estratto di vaniglia pura (o 1 bacca di vaniglia)",
      "Un pizzico di sale",
      "— Aggiunte a piacere (scegli una) —",
      "100g amaretti sbriciolati",
      "80g pistacchi tostati e tritati",
      "100g gocce di cioccolato fondente o cioccolato a scaglie",
      "3 cucchiai di espresso (per il semifreddo al caffè)",
    ],
    "steps": [
      "Rivesti uno stampo da plumcake 23x12cm con pellicola trasparente, lasciando ampia sporgenza su tutti i lati — servirà per sformare il semifreddo.",
      "Sbatti i tuorli d'uovo con metà dello zucchero (75g) usando uno sbattitore elettrico per 5-6 minuti finché diventano chiari, densi, a nastro e raddoppiati di volume. Aggiungi la vaniglia.",
      "In una ciotola fredda separata, monta la panna fredda a picchi morbidi-medi — deve mantenere la forma ma non essere rigida.",
      "In un'altra ciotola pulita, monta gli albumi con un pizzico di sale a picchi morbidi. Aggiungi gradualmente i restanti 75g di zucchero continuando a montare. Continua finché ottieni una meringa lucida e ferma.",
      "Incorpora delicatamente la panna montata al composto di tuorli in 2 riprese — usa una spatola larga con movimenti di ripiegamento leggeri.",
      "Incorpora la meringa al composto cremoso in 3 riprese — è questo che crea la texture leggera e simile alla mousse. Non sgonfiare.",
      "Incorpora l'aggiunta scelta (amaretti, pistacchi, cioccolato o espresso).",
      "Versa nello stampo preparato. Ripiega la pellicola sopra. Congela per almeno 6 ore, idealmente tutta la notte.",
      "Per servire: scarta la pellicola dalla superficie, capovolgi con decisione su un piatto da portata. Rimuovi la pellicola. Affetta con un coltello caldo (passato sotto acqua calda). Servi subito.",
    ],
    "tips": [
      "Tutti i recipienti e gli utensili devono essere perfettamente puliti e freddi per montare correttamente.",
      "Incorpora sempre con movimenti di ripiegamento, mai mescolando — il ripiegamento conserva l'aria che rende il semifreddo leggero.",
      "Un coltello caldo (immerso in acqua calda) affetta in modo netto senza trascinare.",
      "Servi entro 5 minuti dallo sformo — si ammorbidisce rapidamente.",
    ],
    "prose1_h2": "Cosa Distingue il Semifreddo dal Gelato",
    "prose1": "Il gelato viene mantecato durante il congelamento per rompere i cristalli di ghiaccio, creando una consistenza liscia e densa. Il semifreddo raggiunge una morbidezza simile attraverso un metodo completamente diverso: panna montata, uova sbattute e meringa vengono incorporate insieme, inglobando così tanta aria che il composto congela in uno stato cremoso, leggero, simile alla mousse. Senza mantecatura. Il risultato è più morbido e spumoso del gelato, con una consistenza tipicamente italiana — si affetta in modo netto ma si scioglie in modo voluttuoso in bocca.",
    "prose2_h2": "Varianti di Gusto per il Semifreddo",
    "prose2": "La ricetta base è neutra — il che la rende infinitamente versatile. Il semifreddo al pistacchio è la versione italiana più famosa: incorpora 80g di pasta di pistacchio e pistacchi tostati tritati. Caffè e cioccolato è spettacolare: aggiungi 3 tazzine di espresso raffreddato e scaglie di cioccolato fondente. Fragola: incorpora 150g di purè di fragole fresche. Amaretto: aggiungi 3 cucchiai di liquore Amaretto e amaretti sbriciolati. Ogni versione usa la stessa base — cambia solo l'aroma.",
    "img2_alt": "Semifreddo affettato su un piatto di marmo che mostra l'interno cremoso al pistacchio e cioccolato",
    "prose3_h2": "Conservazione e Servizio",
    "prose3": "Il semifreddo si conserva in freezer fino a 2 settimane, ben avvolto nella pellicola. Tiralo fuori dal freezer 5 minuti prima di affettarlo per ammorbidirlo leggermente. Servi a fette su piatti freddi — la temperatura del piatto conta. Guarnisci con frutta fresca, un filo di miele, una spolverata di cacao o granella di frutta secca in abbinamento al gusto scelto.",
    "faqs": [
      ("Posso fare il semifreddo senza uova?", "Sì — usa un rapporto di ⅔ panna montata e ⅓ latte condensato zuccherato al posto del composto a base di uova. È più semplice e comunque molto cremoso, anche se meno simile alla mousse. Mescola il latte condensato con gli aromi e incorpora nella panna montata."),
      ("Perché il mio semifreddo è ghiacciato invece di cremoso?", "Il composto non è stato areato abbastanza — la panna, gli albumi o i tuorli non erano stati montati al volume giusto. Tutti e tre i componenti devono avere buon volume prima di essere incorporati. Inoltre, congela per almeno 6 ore — un tempo di congelamento insufficiente può causare cristalli di ghiaccio."),
      ("Ho bisogno di uno stampo da plumcake?", "No — va bene qualsiasi contenitore adatto al congelatore. Piccoli stampini singoli o stampi in silicone creano belle porzioni individuali. Uno stampo a cerniera rotondo crea una torta semifreddo. La chiave è rivestire con pellicola trasparente per sformare facilmente."),
      ("Quanto prima del servizio devo toglierlo dal freezer?", "Di solito bastano 5-10 minuti a temperatura ambiente. Deve essere abbastanza fermo da affettarsi in modo netto ma abbastanza morbido da sciogliersi in bocca immediatamente. Il semifreddo si ammorbidisce più velocemente del gelato."),
      ("Il semifreddo con uova crude è sicuro?", "Questa ricetta usa uova crude. Se sei preoccupato, usa uova pastorizzate. In alternativa, scalda i tuorli e lo zucchero a bagnomaria fino a 70°C continuando a sbattere — questo li pastorizza — poi procedi con la ricetta."),
    ],
  },

  # ─── 13 — ribollita recipe ────────────────────────────────
  {
    "slug": "ribollita-recipe",
    "title": "Ricetta Ribollita — L'Autentica Zuppa Toscana di Fagioli e Pane",
    "desc": "La vera ribollita toscana: una zuppa densa e sostanziosa di fagioli cannellini, cavolo nero e pane raffermo — cibo contadino elevato alla perfezione. Per 8 persone, migliora ogni giorno.",
    "tag": "Zuppe", "tag_color": "#00695c", "tag_bg": "#e0f2f1",
    "h1": "Ricetta Ribollita — L'Autentica Zuppa Contadina Toscana che Migliora Ogni Giorno",
    "intro": "Ribollita significa 'riscaldata' in italiano — e questo dice tutto su questo piatto. Una zuppa toscana densa e profondamente appagante fatta con fagioli cannellini, cavolo nero e pane raffermo che ispessisce l'intero tegame fino a creare qualcosa tra una zuppa e uno stufato. È cibo contadino che è diventato uno dei piatti più celebri della Toscana.",
    "prep": "20 min", "cook": "1 ora e 20 min", "total": "1 ora e 40 min",
    "servings": "8 porzioni", "calories": "~310", "difficulty": "Facile",
    "badge_text": "Classico Toscano", "cuisine": "Italiana", "category": "Zuppe",
    "keywords": "ricetta ribollita, ribollita toscana, zuppa di fagioli, zuppa di pane toscana, minestra di verdure italiana",
    "cal_num": "310", "protein": "14g", "fat": "8g", "carbs": "46g",
    "ingredients": [
      "2 lattine (800g totali) fagioli cannellini, sgocciolati",
      "300g cavolo nero (o cavolo riccio comune), coste rimosse",
      "400g pane raffermo con crosta (il pane toscano sciocco è tradizionale), spezzettato",
      "400g pomodori pelati interi San Marzano in scatola",
      "2 zucchine medie, a dadini",
      "2 carote medie, a dadini",
      "3 gambi di sedano, a dadini",
      "1 cipolla grande, a dadini",
      "4 spicchi d'aglio, tritati finemente",
      "100g crosta di Parmigiano Reggiano",
      "1,5 litri (6 tazze) brodo vegetale o di pollo",
      "6 cucchiai di olio extravergine d'oliva, più per servire",
      "1 rametto di rosmarino · 2 foglie di alloro",
      "Sale, pepe nero, peperoncino in scaglie",
    ],
    "steps": [
      "In un tegame grande dal fondo spesso, scalda 4 cucchiai di olio extravergine a fuoco medio. Aggiungi cipolla, carote e sedano con un pizzico di sale. Cuoci 12 minuti, mescolando di tanto in tanto, finché sono ammorbiditi e iniziano a colorarsi.",
      "Aggiungi aglio, rosmarino, foglie di alloro e peperoncino. Cuoci 2 minuti finché sono fragranti.",
      "Aggiungi le zucchine e cuoci 5 minuti. Aggiungi i pomodori pelati schiacciati e mescola. Cuoci 10 minuti.",
      "Aggiungi metà dei fagioli cannellini interi. Frulla o schiaccia con una forchetta la metà restante e aggiungila — questo ispessisce la zuppa naturalmente.",
      "Aggiungi il brodo e la crosta di Parmigiano. Porta a sobbollire.",
      "Aggiungi il cavolo nero e mescola finché appassisce nella zuppa. Sobbollisci 30 minuti.",
      "Aggiungi il pane raffermo spezzettato. Mescola bene. Il pane assorbirà il liquido e ispessirà notevolmente la zuppa. Sobbollisci altri 20 minuti, mescolando di tanto in tanto. La consistenza deve essere molto densa — quasi porridge.",
      "Rimuovi rosmarino, foglie di alloro e crosta di Parmigiano. Aggiusta di sale e pepe. Versa nei piatti. Irrora generosamente con il tuo miglior olio extravergine. Facoltativo: servi con Parmigiano grattugiato.",
    ],
    "tips": [
      "Usa pane raffermo — il pane fresco si disintegra. Il pane del giorno prima di un forno è l'ideale.",
      "La crosta di Parmigiano è essenziale — conferisce un profondo umami saporito al brodo.",
      "Schiaccia metà dei fagioli — questo ispessisce la zuppa senza aggiungere amidi.",
      "La ribollita è sempre migliore riscaldata — preparala il giorno prima.",
    ],
    "prose1_h2": "Il Significato di 'Ribollita' e Perché Migliora",
    "prose1": "Ribollita significa letteralmente 'riscaldata' — perché la zuppa veniva tradizionalmente preparata il sabato dai resti della minestrone, poi ribollita la domenica e il lunedì. Ogni riscaldamento fa assorbire al pane più liquido, i fagioli si disfano ulteriormente e i sapori si fondono più in profondità. Al terzo giorno, quella che era una zuppa è diventata qualcosa di più simile a un denso porridge di fagioli e pane. Le nonne toscane considerano la ribollita del terzo giorno la versione migliore. Prepara una grande quantità e verificalo tu stesso.",
    "prose2_h2": "Il Pane Giusto Fa la Differenza",
    "prose2": "La ribollita si prepara tradizionalmente con il pane sciocco — il pane toscano non salato, volutamente neutro perché è fatto per assorbire i sapori piuttosto che aggiungerne di propri. Fuori dalla Toscana, qualsiasi buon pane a lievitazione naturale o pane di campagna va bene. Il pane deve essere raffermo — di almeno un giorno. Il pane fresco si disintegra troppo rapidamente creando una consistenza collosa. I pezzi strappati a mano invece delle fette è la tecnica corretta.",
    "img2_alt": "Densa ribollita in una ciotola di terracotta irrorata di olio extravergine d'oliva e Parmigiano",
    "prose3_h2": "Conservazione e l'Effetto 'Ribollita'",
    "prose3": "La ribollita si conserva in frigorifero per 5 giorni. Ogni riscaldamento la migliora. Per riscaldarla: aggiungi un goccio d'acqua o brodo (si addensa notevolmente da fredda), scalda a fuoco medio-basso mescolando. La ribollita si congela bene per 3 mesi. Scongela in frigorifero durante la notte e riscalda con liquido aggiuntivo.",
    "faqs": [
      ("Cos'è il cavolo nero e posso sostituirlo?", "Il cavolo nero è il cavolo toscano — una verdura a foglia scura e leggermente amara con un sapore robusto. È la scelta tradizionale per la ribollita e si trova nella maggior parte dei supermercati. Il cavolo riccio comune è il miglior sostituto. Funziona anche la verza, anche se è più delicata."),
      ("La ribollita è vegetariana?", "La ricetta base può essere facilmente resa vegetariana usando brodo vegetale e omettendo la crosta di Parmigiano. Aggiungi invece un cucchiaio di miso bianco per profondità. Il risultato è ugualmente appagante."),
      ("Che pane usare se non trovo pane toscano?", "Qualsiasi pane a lievitazione naturale raffermo o pane rustico di campagna funziona perfettamente. Le qualità fondamentali sono: raffermo (non fresco), con crosta (non pan carré morbido), e neutro di sapore. Evita pani con semi o sapori forti."),
      ("Perché la mia ribollita è troppo liquida?", "O non hai aggiunto abbastanza pane o il pane non era abbastanza raffermo. Aggiungi altro pane raffermo spezzettato e continua a sobbollire — assorbe liquido rapidamente. Ricorda: la ribollita deve essere molto densa, più simile a uno stufato che a una zuppa."),
      ("Posso fare la ribollita nella slow cooker?", "Sì — cuoci a bassa temperatura per 8 ore o alta per 4 ore. Aggiungi il pane negli ultimi 30 minuti di cottura a temperatura alta. La crosta di Parmigiano va inserita dall'inizio. Il risultato è eccellente e richiede poco lavoro."),
    ],
  },

  # ─── 14 — spaghetti alla nerano ──────────────────────────
  {
    "slug":        "spaghetti-alla-nerano",
    "title":       "Spaghetti alla Nerano Ricetta Originale — La Pasta con le Zucchine di Nerano",
    "desc":        "Scopri la ricetta originale degli spaghetti alla Nerano: zucchine fritte, Provolone del Monaco e basilico. Il piatto campano diventato virale in tutto il mondo.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Spaghetti alla Nerano Ricetta Originale — La Pasta con le Zucchine che Ha Conquistato il Mondo",
    "intro":       "La storia vuole che gli spaghetti alla Nerano siano stati inventati negli anni '50 dalla famiglia Del Cantinone, un ristorante affacciato sul mare nel villaggio di Nerano, nel cuore della Costiera Amalfitana. Diventati virali in tutto il mondo grazie a Stanley Tucci e al suo programma 'Searching for Italy', la ricetta originale rimane semplice, umile e straordinariamente buona: zucchine fritte riposate una notte, Provolone del Monaco mantecato con l'acqua di cottura, basilico fresco. Nient'altro. La perfezione campana.",
    "prep":        "15 min", "cook": "25 min", "total": "40 min",
    "servings":    "4 porzioni", "calories": "~580", "difficulty": "Facile",
    "badge_text":  "Virale",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "spaghetti alla nerano, spaghetti alla nerano ricetta originale, pasta zucchine provolone, ricetta nerano stanley tucci, pasta campana zucchine",
    "cal_num":     "580", "protein": "22g", "fat": "28g", "carbs": "62g",
    "ingredients": [
      "320g spaghetti",
      "4 zucchine medie",
      "200g Provolone del Monaco (o Caciocavallo stagionato), grattugiato",
      "50g Parmigiano Reggiano grattugiato",
      "1 mazzo abbondante di basilico fresco",
      "Olio extravergine d'oliva abbondante (per friggere)",
      "1 spicchio d'aglio",
      "Sale e pepe nero macinato fresco q.b.",
    ],
    "steps": [
      "Il giorno prima: taglia le zucchine a rondelle sottili di 3mm. Friggi in abbondante olio extravergine a 175-180°C fino a doratura intensa e uniforme. Scola su carta assorbente, sala leggermente e lascia riposare in frigorifero tutta la notte — questo passaggio è fondamentale per la cremosità finale.",
      "Il giorno della preparazione: porta a ebollizione abbondante acqua salata. In una padella larga, scalda un filo d'olio con lo spicchio d'aglio schiacciato. Aggiungi le zucchine fritte riposate e qualche foglia di basilico. Scalda a fuoco medio per 3 minuti.",
      "Cuoci gli spaghetti fino a 2 minuti prima del tempo indicato sulla confezione. Conserva almeno 2 mestoli di acqua di cottura amidacea.",
      "Scola gli spaghetti al dente e versali direttamente nella padella con le zucchine calde. Aggiungi un mestolo di acqua di cottura e mescola a fuoco vivo per 1 minuto.",
      "FONDAMENTALE: togli la padella dal fuoco. Aggiungi il Provolone del Monaco grattugiato e inizia a mantecare vigorosamente con una pinza o un cucchiaio di legno, aggiungendo acqua di cottura tiepida un po' alla volta. La crema deve diventare vellutata, lucida, senza grumi.",
      "Aggiungi il Parmigiano grattugiato, abbondante basilico fresco spezzettato a mano e una generosa macinata di pepe nero. Mescola ancora.",
      "Impiatta subito, aggiungi qualche foglia di basilico fresca, un filo d'olio a crudo e servi immediatamente.",
    ],
    "tips": [
      "Le zucchine DEVONO riposare almeno 6 ore (meglio tutta la notte) — diventano più morbide, asciutte e concentrate di sapore, fondamentali per la crema finale.",
      "Il Provolone del Monaco è l'ingrediente chiave: il Caciocavallo stagionato è il miglior sostituto. Evita mozzarella e scamorza.",
      "Manteca sempre fuori dal fuoco — il calore residuo è sufficiente e impedisce al formaggio di diventare gommoso.",
      "L'acqua di cottura deve essere aggiunta tiepida, non bollente: abbassa la temperatura dell'amido e crea la crema perfetta.",
    ],
    "prose1_h2":  "Dal Ristorante del Cantinone al Mondo Intero: La Storia degli Spaghetti alla Nerano",
    "prose1":     """Gli spaghetti alla Nerano nascono negli anni Cinquanta nella piccola baia di Nerano, un villaggio di pescatori incastonato tra i Monti Lattari e il Mare Tirreno, nel cuore della Penisola Sorrentina. La famiglia Del Cantinone, leggendaria nella zona, inventò questo piatto quasi per caso: zucchine abbondanti nel Golfo di Napoli, il Provolone del Monaco prodotto sui monti vicini e la creatività campana. Per decenni rimase un segreto della costiera. Poi, nel 2021, lo chef e scrittore Stanley Tucci lo assaggiò durante la lavorazione della sua serie televisiva "Searching for Italy" e la sua reazione di pura estasi davanti alla telecamera diventò virale in tutto il mondo. Da quel momento, milioni di persone hanno iniziato a cercare la "ricetta originale degli spaghetti alla Nerano". Il piccolo villaggio di 700 anime è diventato una meta gastronomica internazionale.""",
    "prose2_h2":  "Provolone del Monaco: Il Formaggio DOP che Fa la Differenza",
    "prose2":     """Il Provolone del Monaco è un formaggio a pasta filata DOP prodotto esclusivamente nei 13 comuni della Penisola Sorrentina, stagionato almeno 6 mesi in cantine a temperatura controllata. Il suo nome curioso deriva dai casari che scendevano a Napoli avvolti in mantelli scuri che ricordavano le tonache dei monaci. Ha un sapore intenso, leggermente piccante, con note burrosa e lattiche che si sviluppano durante la lunga stagionatura. La sua caratteristica fondamentale è la filatura a caldo che crea quelle proteine elastiche che, quando mantecate con l'acqua di cottura, formano una crema vellutata impossibile da replicare con altri formaggi. Se non lo trovi, il Caciocavallo stagionato (almeno 6 mesi) è l'unico sostituto accettabile.""",
    "img2_alt":   "Primo piano degli spaghetti alla Nerano con la crema di Provolone del Monaco vellutata e le zucchine fritte dorate",
    "prose3_h2":  "Conservazione e Consigli per il Servizio Perfetto",
    "prose3":     """Gli spaghetti alla Nerano non si conservano bene una volta mantecati: il formaggio si indurisce e la pasta si incolla rapidamente. Prepara sempre la quantità esatta per il pasto e servi subito. Le zucchine fritte, al contrario, si possono e si DEVONO preparare il giorno prima — questo passaggio migliora drasticamente il risultato. Alcune varianti moderne aggiungono gamberi saltati o bottarga di muggine grattugiata, ma la versione originale della famiglia Del Cantinone è rigorosamente solo zucchine, formaggio e basilico. Non aggiungere panna, non aggiungere cipolla, non aggiungere limone. La semplicità è la forza di questo piatto.""",
    "faqs": [
      ("Perché le zucchine devono riposare tutta la notte?", "Il riposo in frigorifero elimina l'umidità in eccesso e trasforma la consistenza delle zucchine fritte: diventano più concentrate di sapore, più morbide e, soprattutto, non rilasciano acqua durante la mantecatura — che renderebbe la salsa acquosa invece che cremosa. È il segreto più importante della ricetta originale."),
      ("Posso usare altri formati di pasta?", "Gli spaghetti sono tradizionali perché la loro superficie liscia cattura perfettamente la crema di formaggio. I linguine o gli spaghettoni funzionano altrettanto bene. Evita la pasta corta: la forma lunga è parte dell'identità del piatto e permette una mantecatura più efficace."),
      ("Cosa faccio se non trovo il Provolone del Monaco?", "Il Caciocavallo stagionato (minimo 6 mesi) è il sostituto più vicino per struttura e sapore. In alternativa, puoi usare metà Pecorino Romano e metà Parmigiano Reggiano. Il risultato sarà meno 'campano' ma comunque ottimo. Evita assolutamente mozzarella, scamorza e formaggi freschi."),
      ("Perché la mia crema di formaggio è diventata gommosa e filante?", "Il formaggio è stato aggiunto con la padella ancora sul fuoco o troppo calda. Togli sempre la padella dal fuoco prima di aggiungere il formaggio e aggiungi l'acqua di cottura tiepida (non bollente) a piccole quantità, mescolando rapidamente. La temperatura ideale dell'impasto è 70-75°C."),
      ("È necessario friggere le zucchine o posso grigliarle?", "La frittura profonda è fondamentale: crea una superficie dorata e caramellata che conferisce profondità di sapore e una consistenza specifica impossibile da replicare con la grigliatura. Le zucchine grigliate rilasciano troppa acqua e non creano la stessa consistenza cremosa durante la mantecatura."),
    ],
  },

  # ─── 15 — pasta alla norma ───────────────────────────────
  {
    "slug":        "pasta-alla-norma-ricetta",
    "title":       "Pasta alla Norma Ricetta Siciliana Autentica — Il Piatto di Catania",
    "desc":        "La vera pasta alla Norma siciliana: melanzane fritte, sugo di pomodoro, basilico e ricotta salata. La ricetta autentica di Catania passo dopo passo in italiano.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Pasta alla Norma Ricetta Siciliana Autentica — Il Capolavoro di Catania",
    "intro":       "La pasta alla Norma è uno dei piatti più celebri della cucina siciliana, nato a Catania in onore dell'opera 'Norma' di Vincenzo Bellini. La storia vuole che il commediografo Nino Martoglio, dopo aver assaggiato questo piatto per la prima volta, esclamasse: 'Chista è 'na vera Norma!' — equiparandone la perfezione a quella del capolavoro musicale. Da allora, melanzane fritte, pomodoro fresco, basilico e ricotta salata sono il quartetto perfetto e insostituibile della tavola siciliana.",
    "prep":        "30 min", "cook": "30 min", "total": "1h",
    "servings":    "4 porzioni", "calories": "~520", "difficulty": "Facile",
    "badge_text":  "Siciliana",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "pasta alla norma, pasta alla norma ricetta siciliana autentica, ricetta norma catania, pasta melanzane ricotta salata sicilia, rigatoni alla norma",
    "cal_num":     "520", "protein": "18g", "fat": "22g", "carbs": "65g",
    "ingredients": [
      "320g rigatoni (o spaghetti)",
      "2 melanzane viola medie (circa 600g)",
      "400g pomodori pelati San Marzano DOP",
      "100g ricotta salata stagionata (grattugiata grossolanamente)",
      "1 spicchio d'aglio",
      "10 foglie di basilico fresco",
      "Olio extravergine d'oliva abbondante (per friggere le melanzane)",
      "Sale e pepe nero q.b.",
    ],
    "steps": [
      "Taglia le melanzane a cubetti di 2cm. Sistemale in uno scolapasta, cospargile di sale grosso e lascia riposare 30 minuti per eliminare l'amaro e l'acqua in eccesso. Sciacqua abbondantemente sotto acqua fredda e asciuga perfettamente con carta assorbente.",
      "Friggi le melanzane in abbondante olio extravergine a 180°C (in più riprese, senza sovraffollare la padella) finché sono ben dorate all'esterno e morbide e fondenti dentro, circa 4-5 minuti per ogni ripresa. Scola su carta assorbente.",
      "In una padella capiente, scalda 3 cucchiai di olio extravergine con lo spicchio d'aglio schiacciato. Quando l'aglio è dorato, aggiungi i pomodori pelati schiacciati con le mani. Cuoci a fuoco medio-vivace per 20 minuti mescolando, fino ad avere un sugo denso, profumato e di colore rosso intenso. Sala, aggiungi qualche foglia di basilico.",
      "Aggiungi metà delle melanzane fritte al sugo e cuoci insieme per 5 minuti a fuoco basso, lasciando insaporire.",
      "Cuoci i rigatoni in abbondante acqua bollente salata fino al dente. Conserva un mestolo di acqua di cottura prima di scolare.",
      "Scola la pasta e versala nella padella con il sugo e le melanzane. Manteca a fuoco vivace per 1-2 minuti aggiungendo un goccio di acqua di cottura se necessario.",
      "Impiatta aggiungendo sopra le melanzane fritte rimaste, abbondante ricotta salata grattugiata grossolanamente e foglie di basilico fresco. Servi subito.",
    ],
    "tips": [
      "La ricotta salata è IRRINUNCIABILE e non sostituibile: non usare ricotta fresca (troppo delicata), né Parmigiano (troppo neutro). Il Pecorino Romano stagionato è l'unico sostituto accettabile.",
      "Le melanzane devono essere fritte in abbondante olio caldo, non saltate con poco olio: la frittura profonda è la tecnica tradizionale siciliana.",
      "Il riposo delle melanzane sotto sale è fondamentale: elimina l'amaro e riduce l'assorbimento di olio in frittura.",
      "D'estate usa pomodori freschi maturi (datterini o San Marzano): il sugo sarà superiore. In inverno, i pelati DOP sono la scelta corretta.",
    ],
    "prose1_h2":  "L'Opera Lirica che Ha Dato il Nome a un Piatto: La Storia della Pasta alla Norma",
    "prose1":     """Catania, fine Ottocento. Il commediografo e poeta dialettale Nino Martoglio siede a tavola davanti a un piatto fumante di pasta con melanzane fritte, sugo di pomodoro e ricotta salata. Dopo il primo boccone, alza gli occhi e pronuncia la frase che è entrata nella storia della cucina italiana: 'Chista è 'na vera Norma!' — in dialetto catanese, 'Questa è una vera Norma!'. Il riferimento era inequivocabile: l'opera 'Norma' di Vincenzo Bellini, il più grande compositore catanese, considerata il capolavoro assoluto del belcanto italiano del XIX secolo. Equiparare un piatto di pasta a un'opera lirica può sembrare eccessivo. Ma a Catania, dove il cibo è cultura e tradizione, era il massimo degli elogi possibili. Da quel momento, il piatto porta orgogliosamente il nome dell'opera. In dialetto siciliano, 'una Norma' è sinonimo di perfezione.""",
    "prose2_h2":  "La Ricotta Salata: L'Ingrediente Identitario e Insostituibile della Norma Autentica",
    "prose2":     """La ricotta salata è un formaggio a pasta dura ottenuto dalla salatura e stagionatura prolungata della ricotta fresca di pecora. Ha un sapore intenso, deciso, leggermente salato e acidulo, con una consistenza granulosa e compatta che si presta perfettamente alla grattugia grossolana. È prodotta in tutta la Sicilia ma quella delle province di Palermo, Agrigento e Ragusa è considerata la migliore per questo piatto. Fuori dalla Sicilia si trova nei negozi specializzati di formaggi italiani, nelle enoteche e online. Non sostituirla mai con ricotta fresca (troppo delicata, umida e insapore), né con Parmigiano Reggiano (troppo neutro e dolce) né con Pecorino fresco. Il Pecorino Romano stagionato è l'unico sostituto accettabile in caso di assoluta necessità — ma il risultato sarà diverso dall'originale catanese.""",
    "img2_alt":   "Pasta alla Norma nel piatto: rigatoni con melanzane fritte lucide, sugo di pomodoro rosso brillante e neve di ricotta salata grattugiata",
    "prose3_h2":  "Varianti Regionali, Conservazione e il Formato di Pasta Autentico",
    "prose3":     """A Catania la pasta alla Norma si prepara tradizionalmente con i rigatoni: i loro 'rigati' longitudinali trattengono perfettamente il sugo di pomodoro e le scaglie di ricotta salata. Nel resto della Sicilia si usano anche gli spaghetti, i maccheroni e la pasta corta in generale. Alcune versioni di Palermo aggiungono una foglia di menta fresca insieme al basilico — una variante inusuale ma autentica nella tradizione palermitana. La pasta alla Norma si conserva in frigorifero per 2 giorni ma perde inevitabilmente la croccantezza delle melanzane fritte. Per conservarla al meglio, tieni il sugo separato dalle melanzane fritte e unisci solo al momento di servire. Non congelare mai la pasta già condita.""",
    "faqs": [
      ("Posso preparare la pasta alla Norma senza friggere le melanzane?", "Tecnicamente sì, ma non sarà più la Norma autentica. Le melanzane al forno assorbono meno olio ma hanno una consistenza più asciutta e un sapore meno intenso. La frittura profonda in abbondante olio caldo crea quella superficie dorata caramellata e quella morbidezza interna fondente che rendono il piatto iconico. È la tecnica tradizionale siciliana e non ha sostituti all'altezza."),
      ("Quale formato di pasta è il più autentico?", "I rigatoni sono la scelta tradizionale di Catania: i loro 'rigati' trattengono perfettamente il sugo denso. Gli spaghetti sono diffusi nel resto della Sicilia. Entrambi sono autentici. Evita assolutamente la pasta fresca all'uovo: la pasta di semola di grano duro è la tradizione siciliana."),
      ("Come riconosco una buona ricotta salata al mercato?", "Una buona ricotta salata deve essere compatta e dura al tatto (deve resistere alla pressione delle dita), di colore bianco-avorio con una crosta esterna più scura, e al sapore deve essere decisa, sapida e leggermente acidula. Evita le versioni troppo fresche o morbide: non si grattugiano correttamente e si sgretolano nel piatto invece di creare quella 'neve' caratteristica."),
      ("Pomodori pelati o freschi per il sugo?", "D'estate (giugno-settembre), usa sempre pomodori freschi maturi — preferibilmente datterini siciliani, San Marzano o costoluti: il sugo sarà superiore per sapore e profumo. Il resto dell'anno, i pomodori pelati San Marzano DOP danno risultati eccellenti. Non usare mai polpa di pomodoro a cubetti: è troppo acquosa."),
      ("Perché le mie melanzane assorbono troppo olio in frittura?", "Ci sono due cause principali: l'olio non era abbastanza caldo (deve essere a 180°C costanti — usa un termometro) oppure le melanzane non erano asciugate perfettamente dopo il riposo sotto sale. L'umidità residua fa abbassare istantaneamente la temperatura dell'olio e le melanzane lo assorbono come spugne. Asciuga sempre accuratamente con carta assorbente prima di friggere."),
    ],
  },

  # ─── 16 — torta caprese ──────────────────────────────────
  {
    "slug":        "torta-caprese-ricetta",
    "title":       "Torta Caprese Ricetta Originale Senza Farina — Il Dolce dell'Isola di Capri",
    "desc":        "La vera torta caprese senza farina: cioccolato fondente 70%, mandorle, burro e uova. Umida dentro, crosticina fuori. La ricetta originale di Capri passo dopo passo.",
    "tag":         "Dolci",
    "tag_color":   "#6a1b9a",
    "tag_bg":      "#f3e5f5",
    "h1":          "Torta Caprese Ricetta Originale Senza Farina — Il Dolce di Capri",
    "intro":       "La torta caprese è nata per errore. Secondo la leggenda, negli anni Venti un pasticcere dell'isola di Capri di nome Carmine Di Fiore stava preparando una torta di mandorle per alcuni ospiti americani e dimenticò di aggiungere la farina. Invece di buttare l'impasto, lo infornò comunque — e nacque uno dei dolci italiani più amati al mondo. Naturalmente senza farina, naturalmente gluten-free, con una crosticina leggermente croccante fuori e un cuore umido e intenso di cioccolato fondente e mandorle dentro. Il dolce più famoso di Capri.",
    "prep":        "20 min", "cook": "35 min", "total": "55 min",
    "servings":    "8 porzioni", "calories": "~420", "difficulty": "Facile",
    "badge_text":  "Senza Farina",
    "cuisine":     "Italiana",
    "category":    "Dolci",
    "keywords":    "torta caprese ricetta originale, torta caprese senza farina, ricetta torta caprese, dolce caprese cioccolato mandorle, torta caprese gluten free",
    "cal_num":     "420", "protein": "9g", "fat": "30g", "carbs": "32g",
    "ingredients": [
      "200g cioccolato fondente (minimo 70% di cacao), tritato",
      "200g burro non salato, morbido a temperatura ambiente",
      "200g zucchero semolato",
      "200g farina di mandorle (o mandorle pelate frullate finemente)",
      "4 uova grandi, a temperatura ambiente",
      "1 cucchiaino di estratto naturale di vaniglia",
      "1 pizzico generoso di sale fino",
      "Zucchero a velo q.b. per decorare",
    ],
    "steps": [
      "Preriscalda il forno a 170°C (statico). Imburra abbondantemente uno stampo rotondo da 24cm e rivesti il fondo con carta forno.",
      "Sciogli il cioccolato fondente a bagnomaria (a fuoco bassissimo, senza far toccare l'acqua al pentolino) oppure nel microonde a intervalli di 30 secondi, mescolando ogni volta. Lascia raffreddare fino a temperatura ambiente — non deve essere caldo quando lo unisci alle uova.",
      "In una ciotola capiente, sbatti il burro morbido con lo zucchero usando le fruste elettriche per 3-4 minuti, fino a ottenere un composto chiaro, spumoso e quasi bianco.",
      "Aggiungi le uova al composto di burro, una alla volta, aspettando che ogni uovo sia completamente incorporato prima di aggiungere il successivo. Se il composto sembresse 'granuloso', è normale — si compatterà con il cioccolato.",
      "Aggiungi il cioccolato fuso raffreddato e la vaniglia. Mescola con una spatola fino a ottenere un composto liscio e lucido.",
      "Incorpora la farina di mandorle e il pizzico di sale. Mescola delicatamente con movimenti dal basso verso l'alto fino a ottenere un impasto omogeneo, denso e profumato.",
      "Versa l'impasto nello stampo preparato e livella la superficie con una spatola. Cuoci in forno preriscaldato per 30-35 minuti: la torta è pronta quando la superficie ha una crosticina solida che non cede alla pressione del dito, ma il centro trema ancora leggermente quando muovi lo stampo. NON cuocere oltre: l'umidità interna è la caratteristica fondamentale.",
      "Lascia raffreddare completamente nello stampo (almeno 1 ora) prima di sformare. Capovolgi su un piatto da portata, rimuovi la carta forno e cospargi abbondantemente di zucchero a velo prima di servire.",
    ],
    "tips": [
      "Non cuocere troppo: il segreto della torta caprese è la consistenza umida e fondente dentro. Il centro deve tremare leggermente all'uscita dal forno — si solidificherà raffreddandosi.",
      "Usa cioccolato fondente di qualità con almeno 70% di cacao: è l'ingrediente principale e fa tutta la differenza nel sapore finale.",
      "La torta caprese migliora notevolmente il giorno dopo: preparala la sera per servirla il giorno seguente.",
      "Per una versione più intensa e adulta, aggiungi 1 cucchiaio di rum, whisky o liquore Limoncello di Capri all'impasto prima di infornare.",
    ],
    "prose1_h2":  "La Leggenda del Pasticcere Smemorato: Come è Nata la Torta Caprese",
    "prose1":     """Siamo nell'estate del 1920, sull'isola di Capri. Carmine Di Fiore, pasticcere locale ben noto sull'isola, riceve una commissione importante: preparare una torta di mandorle per alcuni facoltosi ospiti americani in visita sull'isola. Preso dalla fretta e forse dalla distrazione del panorama mozzafiato del Golfo di Napoli, inforna l'impasto dimenticando di aggiungere la farina. Aspettandosi un disastro quando apre il forno, sforna invece una torta diversa da tutto ciò che conosce: densa, umida, con una crosticina leggermente croccante in superficie e un cuore fondente e intensissimo di cioccolato e mandorle. Gli ospiti americani la adorano. La voce si sparge rapidamente sull'isola. Il 'dimenticato' diventa il 'segreto'. Carmine inizia a prepararla intenzionalmente. Oggi, oltre un secolo dopo, la torta caprese è servita in tutti i ristoranti di Capri, in tutta Italia e in tutto il mondo — sempre rigorosamente senza farina, proprio come quella prima volta per errore.""",
    "prose2_h2":  "Perché la Torta Caprese è Naturalmente Gluten-Free e Perché Funziona Senza Farina",
    "prose2":     """La torta caprese non contiene farina di grano — e non perché sia stata adattata per diete speciali o per seguire tendenze moderne, ma perché la ricetta originale non l'ha mai prevista. Le mandorle tritate finemente forniscono struttura e umidità grazie al loro elevato contenuto di grassi naturali (circa 50% di grassi buoni), mentre il cioccolato fondente ricco di burro di cacao lega il tutto creando una consistenza densa e umida che la farina non potrebbe mai replicare. È la combinazione chimica di grassi delle mandorle, burro di cacao del cioccolato e proteine delle uova che rende possibile una torta senza farina così soddisfacente. Questo la rende adatta a chi segue una dieta senza glutine senza alcuna modifica alla ricetta originale. Per garantire la sicurezza delle persone celiache, è importante utilizzare cioccolato fondente certificato gluten-free e mandorle prodotte in stabilimenti privi di contaminazione crociata.""",
    "img2_alt":   "Torta caprese tagliata mostrando il cuore umido e fondente di cioccolato e mandorle, con abbondante zucchero a velo bianco in superficie",
    "prose3_h2":  "Conservazione, Varianti Famose e la Versione Bianca di Capri",
    "prose3":     """La torta caprese si conserva perfettamente a temperatura ambiente sotto una campana di vetro o in un contenitore ermetico per 3-4 giorni — migliorando ogni giorno che passa. In frigorifero dura fino a 7 giorni: tirala fuori almeno 30 minuti prima di servire per riportarla a temperatura ambiente e ritrovare la consistenza fondente. Si congela eccellentemente per 3 mesi, intera o già tagliata a fette singole: scongela in frigorifero durante la notte. Tra le varianti più famose e apprezzate dell'isola c'è la torta caprese bianca al limone: stessa struttura, ma con cioccolato bianco invece del fondente e il profumo del limone di Capri IGP al posto della vaniglia. Altre varianti moderne includono la versione al pistacchio di Bronte (con farina di pistacchi verdi siciliani invece delle mandorle) e la versione con arancia candita e cannella, tipica del periodo natalizio.""",
    "faqs": [
      ("Posso usare le mandorle con la buccia invece di quelle pelate?", "Sì, ma il risultato sarà più rustico nel sapore e nell'aspetto. Le mandorle con buccia hanno un sapore più intenso e leggermente amaro e conferiscono alla torta un colore più scuro. Per la versione tradizionale di Capri si usano mandorle pelate. Se hai solo mandorle con buccia, frullale comunque finemente: la torta risulterà ugualmente buona, semplicemente con un carattere più deciso."),
      ("Come capisco se la torta caprese è cotta al punto giusto?", "La superficie deve avere una crosticina solida che non cede alla pressione del dito, ma il centro deve muoversi leggermente quando scuoti delicatamente lo stampo. Un termometro da cottura inserito al centro deve segnare 85-88°C. Se aspetti che il centro sia completamente fermo, l'avrai cotta troppo e perderà la sua caratteristica umidità interna fondente."),
      ("Posso sostituire le mandorle con altri frutti secchi?", "Il pistacchio di Bronte è la variante più famosa e deliziosa. Le nocciole funzionano molto bene creando qualcosa di simile a una torta al cioccolato Ferrero. Le noci creano una versione più amara e intensa. Evita i pinoli: sono troppo delicati, oleosi e non danno la struttura necessaria. Con i pistacchi, riduci lo zucchero di 20g perché sono naturalmente più dolci."),
      ("La torta caprese si gonfia durante la cottura?", "No — non contiene agenti lievitanti (né lievito né bicarbonato) e non si gonfia in forno. Si alza leggermente durante la cottura grazie all'aria incorporata nelle uova, poi si affloscia raffreddandosi: questo è normale e assolutamente desiderato. Quella 'caduta' crea la caratteristica superficie incrinata e la crosticina croccante che la rendono riconoscibile."),
      ("Posso preparare la torta caprese in anticipo?", "Assolutamente sì — è anzi vivamente consigliato. Preparata 12-24 ore prima, gli aromi del cioccolato e delle mandorle si intensificano, la consistenza umida si stabilizza perfettamente e la crosticina si consolida. È uno dei dolci italiani più adatti alla preparazione anticipata, perfetto per i pranzi e le cene del giorno dopo."),
    ],
  },

  # ─── 17 — pasta e fagioli ────────────────────────────────
  {
    "slug":        "pasta-e-fagioli-ricetta",
    "title":       "Pasta e Fagioli Ricetta Napoletana Originale — La Zuppa della Tradizione",
    "desc":        "La vera pasta e fagioli napoletana: fagioli borlotti, pasta mista, soffritto e rosmarino. Ricetta originale della nonna campana, densa e saporita come vuole la tradizione.",
    "tag":         "Zuppe",
    "tag_color":   "#2e7d32",
    "tag_bg":      "#e8f5e9",
    "h1":          "Pasta e Fagioli Ricetta Napoletana Originale — La Zuppa della Tradizione",
    "intro":       "La pasta e fagioli è forse il piatto più umile e più amato della cucina italiana — un piatto di sopravvivenza diventato capolavoro. La versione napoletana è la più famosa: densa come una crema, con i fagioli borlotti parzialmente frullati che creano una consistenza vellutata, la pasta mista che si cuoce direttamente nel brodo di fagioli, il rosmarino che profuma tutta la casa. Non è una minestra, non è un primo, non è un secondo: è un piatto unico che basta a sé stesso e nutre l'anima.",
    "prep":        "15 min", "cook": "1h 30min", "total": "1h 45min",
    "servings":    "6 porzioni", "calories": "~380", "difficulty": "Facile",
    "badge_text":  "Tradizione",
    "cuisine":     "Italiana",
    "category":    "Zuppe",
    "keywords":    "pasta e fagioli ricetta napoletana originale, pasta e fagioli ricetta, pasta fagioli napoletana, ricetta pasta fagioli della nonna, zuppa fagioli borlotti pasta",
    "cal_num":     "380", "protein": "16g", "fat": "10g", "carbs": "58g",
    "ingredients": [
      "400g fagioli borlotti secchi (oppure 800g in scatola ben sciacquati)",
      "200g pasta mista (o ditalini, tubetti, spaghetti spezzati)",
      "1 cipolla dorata media",
      "2 spicchi d'aglio",
      "2 gambi di sedano",
      "1 carota",
      "2 rametti di rosmarino fresco",
      "400g pomodori pelati",
      "4 cucchiai di olio extravergine d'oliva + extra per servire",
      "Sale e pepe nero q.b.",
      "Parmigiano Reggiano grattugiato per servire",
    ],
    "steps": [
      "Se usi fagioli secchi: mettili in ammollo in abbondante acqua fredda per 12 ore. Scolali, sciacquali e cuocili in abbondante acqua non salata per 60-70 minuti finché sono teneri. Conserva l'acqua di cottura. Se usi fagioli in scatola, salta questo passaggio.",
      "Prepara il soffritto: in una pentola capiente, scalda l'olio extravergine a fuoco medio. Aggiungi la cipolla tritata finemente, il sedano e la carota a dadini piccoli. Cuoci mescolando per 8-10 minuti fino a doratura leggera e morbidezza.",
      "Aggiungi gli spicchi d'aglio interi schiacciati e i rametti di rosmarino. Cuoci per 2 minuti fino a che l'aglio è dorato e il rosmarino profuma. Rimuovi il rosmarino e l'aglio se preferisci un sapore delicato.",
      "Aggiungi i pomodori pelati schiacciati con le mani. Cuoci a fuoco vivace per 5 minuti mescolando, fino a che il sugo si ritira e si addensa.",
      "Aggiungi i fagioli cotti con tutta la loro acqua di cottura (o aggiunta acqua calda se usi quelli in scatola — circa 1,5 litri totali). Porta a ebollizione, abbassa la fiamma e cuoci per 20 minuti.",
      "FONDAMENTALE: con un mestolo forato, preleva circa la metà dei fagioli e frullali con un frullatore a immersione (o nel frullatore). Rimetti il purè nella pentola e mescola: il brodo diventerà denso e cremoso.",
      "Porta di nuovo a bollore, aggiusta di sale. Aggiungi la pasta mista direttamente nella zuppa e cuoci mescolando spesso fino al dente — circa 10-12 minuti a seconda del formato scelto.",
      "Servi subito con un filo generoso di olio extravergine crudo, pepe nero macinato fresco e abbondante Parmigiano grattugiato.",
    ],
    "tips": [
      "La pasta va cotta direttamente nella zuppa, non a parte — rilascia amido che rende il piatto ancora più denso e saporito.",
      "Frullare metà dei fagioli è il segreto della consistenza cremosa tipica napoletana: non saltare questo passaggio.",
      "La pasta e fagioli si addensa notevolmente raffreddandosi: aggiunge un mestolo d'acqua calda quando la riscaldi.",
      "Con fagioli secchi il sapore è nettamente superiore: vale i 12 ore di ammollo in più.",
    ],
    "prose1_h2":  "Il Piatto Più Povero e Più Ricco d'Italia: Storia della Pasta e Fagioli",
    "prose1":     """La pasta e fagioli è nata dalla necessità. Nell'Italia rurale del passato, fagioli e pasta erano gli ingredienti più economici e nutrienti a disposizione delle famiglie contadine. A Napoli, dove la miseria era parte quotidiana della vita nei vicoli, questo piatto è diventato un'istituzione: il 'piatto del proletariato' che nutriva famiglie intere con pochissimo. I macellai napoletani conservavano le cotiche di maiale e le ossa avanzate proprio per aggiungere profondità al brodo della pasta e fagioli — e così questo piatto di sopravvivenza è diventato, nei secoli, un capolavoro di sapori. Oggi la pasta e fagioli è servita nei ristoranti stellati e nelle trattorie popolari con la stessa dignità. Il segreto è sempre lo stesso: tempo, pazienza e buoni ingredienti.  """,
    "prose2_h2":  "Fagioli Secchi o in Scatola: La Differenza nel Piatto",
    "prose2":     """La differenza tra fagioli secchi e fagioli in scatola in questo piatto è enorme. I fagioli secchi, cotti lentamente nella loro acqua, rilasciano una quantità di amido naturale e sapore che i fagioli in scatola (già cotti e conservati in acqua) non possono replicare. L'acqua di cottura dei fagioli secchi è il vero 'brodo segreto' della pasta e fagioli napoletana — densa, amidacea, con un sapore terroso e vegetale che forma la base dell'intera zuppa. I fagioli borlotti sono la scelta tradizionale napoletana: la loro consistenza cremosa e il loro sapore delicatamente dolce li rendono perfetti per questo piatto. I fagioli cannellini danno una versione più delicata; i fagioli bianchi di Spagna una più robusta.""",
    "img2_alt":   "Ciotola fumante di pasta e fagioli napoletana con un filo d'olio extravergine, pepe nero e Parmigiano grattugiato",
    "prose3_h2":  "Conservazione, Varianti Regionali e il Giorno Dopo",
    "prose3":     """La pasta e fagioli si conserva in frigorifero per 3-4 giorni. Il giorno dopo è ancora più buona — i sapori si fondono e si intensificano durante la notte. Quando la riscaldi, aggiunge sempre un mestolo di acqua calda o brodo perché si addensa molto. La versione veneta aggiunge pancetta affumicata nel soffritto; quella toscana usa fagioli cannellini e salvia invece del rosmarino; quella romana include rigatoni e una crosta di Parmigiano intera nella zuppa. La versione più 'ricca' napoletana aggiunge cotiche di maiale o piedino di maiale per un sapore più profondo — tipica dei giorni di festa. Tutte le versioni sono autentiche: la pasta e fagioli è il piatto dell'Italia intera.""",
    "faqs": [
      ("Posso usare altri tipi di fagioli?", "Sì — i fagioli cannellini danno una versione più delicata e cremosa; i fagioli di Spagna una più rustica e saporita; i fagioli neri una versione moderna e di carattere. I borlotti restano la scelta tradizionale napoletana per il loro equilibrio perfetto tra cremosità e sapore."),
      ("Perché la mia pasta e fagioli è diventata troppo densa?", "La pasta assorbe liquido continuando a cuocere. Se la zuppa è troppo densa, aggiungi acqua calda o brodo caldo mescolando fino alla consistenza desiderata. La pasta e fagioli napoletana deve essere 'azzeccata' — densa — ma non deve diventare una palla solida."),
      ("Posso prepararla in anticipo?", "Sì, ma con un accorgimento: cuoci i fagioli e il soffritto in anticipo (si conserva 3-4 giorni), ma aggiungi la pasta solo al momento di servire. La pasta già cotta diventa molle e gommosa il giorno dopo."),
      ("La pancetta è necessaria?", "No — la ricetta napoletana tradizionale più povera è rigorosamente vegetariana (olio, verdure, fagioli, pasta). La pancetta o le cotiche di maiale sono aggiunte delle versioni più 'ricche'. Omettila per una versione vegana sostituendo il Parmigiano con lievito alimentare in scaglie."),
      ("Quale pasta usare?", "La pasta mista — i scarti e gli avanzi di diversi formati mescolati insieme — è la scelta tradizionale napoletana autentica. I ditalini rigati, i tubetti, i ditali sono le alternative più usate. Lo spaghetto spezzato è comune in alcune zone della Campania. Evita la pasta lunga intera: è difficile da mangiare nella zuppa."),
    ],
  },

  # ─── 18 — saltimbocca alla romana ────────────────────────
  {
    "slug":        "saltimbocca-alla-romana",
    "title":       "Saltimbocca alla Romana Ricetta Originale — Il Secondo Piatto di Roma",
    "desc":        "La vera ricetta del saltimbocca alla romana: fettine di vitello, prosciutto crudo, salvia fresca e vino bianco. Pronto in 15 minuti, autentico come a Roma.",
    "tag":         "Secondi",
    "tag_color":   "#c62828",
    "tag_bg":      "#ffebee",
    "h1":          "Saltimbocca alla Romana Ricetta Originale — Il Secondo di Roma Pronto in 15 Minuti",
    "intro":       "Il nome dice tutto: 'salta in bocca'. Il saltimbocca alla romana è uno dei secondi piatti più celebri della cucina laziale — fettine sottili di vitello battute, coperte da una fetta di prosciutto crudo e una foglia di salvia fresca, fermate con uno stuzzicadenti e saltate velocemente in padella con burro e vino bianco. Dieci minuti di cottura, ingredienti semplici, risultato straordinario. La Roma in un piatto.",
    "prep":        "10 min", "cook": "10 min", "total": "20 min",
    "servings":    "4 porzioni", "calories": "~320", "difficulty": "Facile",
    "badge_text":  "15 Min",
    "cuisine":     "Italiana",
    "category":    "Secondi",
    "keywords":    "saltimbocca alla romana ricetta originale, saltimbocca alla romana, ricetta saltimbocca, vitello prosciutto salvia roma, secondo piatto romano veloce",
    "cal_num":     "320", "protein": "35g", "fat": "16g", "carbs": "4g",
    "ingredients": [
      "8 fettine di vitello (scaloppine), circa 600g totali",
      "8 fette di prosciutto crudo di Parma",
      "8 foglie grandi di salvia fresca",
      "40g burro non salato",
      "100ml vino bianco secco (Frascati o Pinot Grigio)",
      "Sale e pepe nero q.b.",
      "Farina 00 q.b. per infarinare leggermente",
    ],
    "steps": [
      "Batti le fettine di vitello tra due fogli di carta forno con un batticarne fino a uno spessore di 4-5mm. Sala e pepa leggermente su entrambi i lati.",
      "Adagia una foglia di salvia fresca su ogni fettina. Coprila con una fetta di prosciutto crudo, premendo leggermente perché aderisca bene alla carne. Ferma tutto con uno stuzzicadenti passato orizzontalmente.",
      "Infarina leggermente il lato della carne (non il prosciutto) passandola nella farina e scrollando l'eccesso.",
      "Scalda il burro in una padella capiente a fuoco medio-alto finché inizia a schiumare. Adagia i saltimbocca con il lato del prosciutto verso il basso. Cuoci per 2-3 minuti finché il prosciutto è croccante e leggermente dorato.",
      "Gira delicatamente i saltimbocca sull'altro lato. Cuoci per 1-2 minuti appena — la carne di vitello è sottile e si cuoce rapidamente.",
      "Alza la fiamma, aggiungi il vino bianco tutto in una volta. Lascia sfumare per 1-2 minuti raschiando i fondini di cottura con un cucchiaio di legno — i fondini sono pieni di sapore.",
      "Togli i saltimbocca dalla padella. Fai ridurre il fondo di cottura per 1 minuto ancora a fuoco vivo fino a ottenere una salsina lucida e nappante. Versa sui saltimbocca e servi subito.",
    ],
    "tips": [
      "Non cuocere troppo il vitello: le fettine sono sottilissime e bastano 2-3 minuti per lato — oltre diventano dure.",
      "Il prosciutto cuoce verso il basso prima, così diventa croccante e trattiene i succhi nella carne.",
      "Non salare il lato del prosciutto: il prosciutto crudo è già salato e sapido.",
      "Il fondo di cottura con il vino bianco è la salsa — non buttarlo mai, è il cuore del piatto.",
    ],
    "prose1_h2":  "Saltimbocca: Un Nome, Una Promessa — La Storia del Piatto Romano",
    "prose1":     """Il saltimbocca alla romana è citato per la prima volta nella letteratura gastronomica italiana nell'800, ma le sue radici sono certamente più antiche. Il nome — 'salta in bocca' — è il più onesto della cucina italiana: descrive esattamente quello che accade quando lo mangi. La combinazione di vitello morbido, prosciutto salato e croccante, e salvia aromatica e leggermente amara è una delle più riuscite della gastronomia mondiale. A Roma il saltimbocca è un piatto quotidiano: si trova nelle trattorie di Testaccio come nelle osterie di Trastevere, preparato sempre con la stessa semplicità e la stessa velocità. Alcune ricette storiche aggiungono la fontina o la mozzarella tra la carne e il prosciutto, ma la versione autentica e più diffusa è quella senza formaggio.""",
    "prose2_h2":  "Il Vitello Giusto e il Prosciutto Giusto: I Due Ingredienti Chiave",
    "prose2":     """Per il saltimbocca romano autentico, la scelta degli ingredienti è tutto. Il vitello deve essere noce o fesa — i tagli più teneri e delicati — tagliati sottili e battuti ulteriormente. Non usare mai maiale o pollo: il sapore delicato del vitello è fondamentale per l'equilibrio del piatto. Il prosciutto di Parma DOP è la scelta classica: dolce, morbido, con la giusta quantità di grasso che si scioglie in cottura avvolgendo la carne. Il prosciutto di San Daniele DOP è altrettanto eccellente. Evita il prosciutto cotto: il sapore è completamente diverso. La salvia deve essere fresca e con foglie grandi e integre — quella secca non funziona, perde profumo e diventa amara.""",
    "img2_alt":   "Saltimbocca alla romana nel piatto con prosciutto croccante, salvia fresca e salsina al vino bianco lucida",
    "prose3_h2":  "Varianti, Accompagnamenti e Conservazione",
    "prose3":     """Il saltimbocca alla romana si serve tradizionalmente con contorni semplici che non rubino la scena: patate al forno, insalata verde, spinaci al burro o carciofi alla romana. Il riso pilaf funziona bene per raccogliere la salsina. Come variante, alcune trattorie romane aggiungono una fetta di provola o fontina tra la carne e il prosciutto prima di cuocere — il formaggio si scioglie parzialmente creando un effetto filante. Il saltimbocca non si conserva bene: è pensato per essere mangiato subito, appena uscito dalla padella. Se avanza, conserva in frigorifero per massimo 24 ore e riscalda delicatamente in padella con un goccio di vino bianco.""",
    "faqs": [
      ("Posso usare pollo invece del vitello?", "Sì — il pollo (petto battuto sottile) è un sostituto accettabile e più economico. Il sapore sarà diverso: meno delicato e più deciso. Aumenta leggermente il tempo di cottura — il pollo richiede circa 4 minuti per lato invece di 2-3. Evita il petto troppo spesso: deve essere battuto fino a 5mm per cuocere rapidamente."),
      ("Perché il mio saltimbocca è diventato duro?", "La carne è stata cotta troppo a lungo. Il vitello ha pochissimi tessuti connettivi e si cuoce in 2-3 minuti per lato. Oltre questo tempo, le proteine si contraggono e la carne diventa dura come cartone. Tieniti alla temperatura giusta (fuoco medio-alto) e non superare i tempi indicati."),
      ("Posso prepararlo senza vino?", "Sì — sostituisci il vino bianco con brodo di pollo o di verdure. Il risultato sarà meno complesso ma comunque buono. Il vino bianco aggiunge un'acidità che bilancia il grasso del burro e la sapidità del prosciutto: è preferibile non omettere completamente la parte liquida."),
      ("Lo stuzzicadenti si toglie prima di servire?", "Sì — togli sempre lo stuzzicadenti prima di impiattare. Fallo con cura per non separare il prosciutto dalla carne. Se preferisci, non usare lo stuzzicadenti e premi semplicemente il prosciutto sulla carne con le dita — aderisce abbastanza bene grazie al grasso naturale."),
      ("Posso aggiungere il formaggio?", "La versione originale non lo prevede. Ma la variante con fontina o provola è diffusa e gustosa: posiziona una fettina sottile di formaggio tra la carne e il prosciutto prima di arrotolare e fissare con lo stuzzicadenti. Il formaggio si scioglie parzialmente durante la cottura."),
    ],
  },

  # ─── 19 — pesto alla genovese ────────────────────────────
  {
    "slug":        "pesto-alla-genovese-ricetta",
    "title":       "Pesto alla Genovese Ricetta Originale — Il Condimento Ligure Autentico",
    "desc":        "La ricetta originale del pesto alla genovese: basilico DOP, pinoli, Parmigiano, Pecorino e aglio nel mortaio. Il vero pesto ligure fatto a mano passo dopo passo.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Pesto alla Genovese Ricetta Originale — Il Condimento Ligure nel Mortaio",
    "intro":       "Il pesto alla genovese è il condimento italiano più imitato e più raramente preparato nel modo giusto. La ricetta originale, depositata dalla Confraternita del Pesto di Genova, richiede basilico Genovese DOP, pinoli tostati, aglio, Parmigiano Reggiano DOP, Pecorino sardo e olio extravergine ligure — lavorati rigorosamente nel mortaio di marmo con il pestello di legno. Il calore delle lame del frullatore ossida il basilico e trasforma il verde brillante in marrone opaco. Il mortaio è lento ma crea una consistenza cremosa e un profumo impossibili da replicare.",
    "prep":        "20 min", "cook": "0 min", "total": "20 min",
    "servings":    "4 porzioni", "calories": "~180", "difficulty": "Facile",
    "badge_text":  "Originale",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "pesto alla genovese ricetta originale, pesto genovese ricetta, ricetta pesto basilico originale, pesto fatto in casa mortaio, pesto ligure autentico",
    "cal_num":     "180", "protein": "5g", "fat": "17g", "carbs": "3g",
    "ingredients": [
      "50g foglie di basilico fresco (preferibilmente basilico Genovese DOP, piccole e profumatissime)",
      "30g pinoli",
      "1 spicchio d'aglio (piccolo)",
      "40g Parmigiano Reggiano DOP, grattugiato finemente",
      "20g Pecorino sardo stagionato, grattugiato finemente",
      "80-100ml olio extravergine d'oliva ligure (o altro delicato)",
      "1 pizzico di sale grosso",
    ],
    "steps": [
      "Lava le foglie di basilico delicatamente in acqua fredda. Asciugale tamponando con un panno morbido — non strofinare, il basilico è delicato e si ossida facilmente. Lascia asciugare completamente su un canovaccio.",
      "Nel mortaio di marmo freddo, pesta lo spicchio d'aglio con il sale grosso fino a ottenere una pasta liscia. Il sale funge da abrasivo.",
      "Aggiungi i pinoli e pesta con movimenti circolari fino a ridurli in crema.",
      "Aggiungi le foglie di basilico a piccole manciate, lavorandole con movimenti rotativi del pestello contro le pareti del mortaio. Non pestare dall'alto: il movimento circolare rompe le cellule del basilico senza scaldarle.",
      "Continua ad aggiungere basilico poco alla volta fino ad esaurimento, lavorando fino ad ottenere una pasta verde brillante e profumatissima.",
      "Aggiungi il Parmigiano e il Pecorino grattugiati. Mescola con il pestello incorporandoli delicatamente nella pasta verde.",
      "Aggiungi l'olio extravergine a filo, mescolando con il pestello fino ad ottenere una salsa omogenea, lucida e cremosa. Assaggia e regola di sale.",
    ],
    "tips": [
      "Usa basilico a foglie piccole, giovane e freschissimo — il basilico Genovese DOP è il più profumato e il meno amaro.",
      "Il mortaio e il pestello devono essere FREDDI: mettili in frigorifero 30 minuti prima se fa caldo. Il calore ossida il basilico.",
      "Se usi il frullatore: usa la funzione pulse (a intermittenza) e aggiungi cubetti di ghiaccio per mantenere la temperatura bassa. Il risultato sarà comunque inferiore al mortaio.",
      "Conserva il pesto con uno strato di olio in superficie in frigorifero per massimo 3 giorni, oppure congelalo in cubetti per 3 mesi.",
    ],
    "prose1_h2":  "La Ricetta Depositata: Il Pesto Genovese nella Storia e nella Tradizione Ligure",
    "prose1":     """Il pesto alla genovese ha radici antichissime nella Liguria medievale: le salse a base di erbe pestate nel mortaio erano comuni in tutta l'area mediterranea. Ma la versione moderna con basilico, pinoli, aglio e formaggio si codifica a Genova nell'Ottocento, quando il porto ligure era uno dei più attivi d'Europa e la cucina genovese si arricchiva degli scambi commerciali. Il termine 'pesto' deriva semplicemente dal verbo 'pestare' — e il mortaio rimane lo strumento identitario della preparazione autentica. Nel 2009 la Confraternita del Pesto di Genova ha depositato la ricetta ufficiale, specificando ogni ingrediente con la sua provenienza geografica precisa. Il Campionato Mondiale del Pesto al Mortaio si svolge ogni due anni a Genova, con concorrenti da tutto il mondo che si sfidano a chi produce il pesto più profumato e cremoso.""",
    "prose2_h2":  "Mortaio vs Frullatore: La Verità Sulla Differenza",
    "prose2":     """La scienza spiega perché il mortaio è superiore al frullatore per il pesto. Le lame metalliche del frullatore girano a velocità altissima generando calore e ossigeno — i due nemici del basilico. Il calore denatura le clorofille e gli enzimi ossidativi del basilico trasformando il colore da verde brillante a verde-marrone opaco in pochi secondi. Il mortaio, al contrario, rompe le cellule vegetali attraverso pressione meccanica lenta, liberando gli oli essenziali del basilico senza surriscaldarli. Il risultato è un pesto più verde, più profumato e con una consistenza granulosa e cremosa al tempo stesso che le lame del frullatore non riescono a creare. Se proprio devi usare il frullatore, usa la funzione a intermittenza, aggiungi cubetti di ghiaccio nel contenitore e lavora in 3-4 riprese di 5 secondi ciascuna.""",
    "img2_alt":   "Mortaio di marmo con pesto alla genovese verde brillante, pinoli e foglie di basilico fresco intorno",
    "prose3_h2":  "Come Usare il Pesto, Conservarlo e le Varianti Liguri",
    "prose3":     """Il pesto alla genovese si usa tradizionalmente con le trofie (pasta ligure attorcigliata) o le trenette (tagliatelle liguri), sempre con patate lessate e fagiolini nella stessa acqua di cottura — la 'pasta al pesto con patate e fagiolini' è il piatto ligure per eccellenza. Importante: non scaldare mai il pesto in padella, aggiungi sempre a freddo alla pasta calda con un po' di acqua di cottura. Il calore distrugge il colore e il profumo. Per conservarlo: ricopri sempre con uno strato di olio extravergine in superficie prima di chiudere il barattolo — previene l'ossidazione. In frigorifero dura 3-4 giorni, nel congelatore 3 mesi (congela in vaschette per il ghiaccio per avere porzioni singole).""",
    "faqs": [
      ("Posso usare il frullatore invece del mortaio?", "Sì, ma il risultato sarà diverso: il pesto diventerà più scuro (verde-marrone) e meno profumato a causa del calore generato dalle lame. Per minimizzare i danni: usa la funzione pulse, lavora in riprese brevi di 5 secondi, aggiungi qualche cubetto di ghiaccio al basilico e metti il contenitore del frullatore nel freezer 10 minuti prima. Il risultato sarà comunque molto buono, anche se non identico al mortaio."),
      ("Perché il mio pesto è diventato nero o marrone?", "Il basilico si è ossidato per il calore (frullatore troppo veloce o troppo a lungo) o per il contatto con l'aria. Per evitarlo: lavora il basilico freddo e asciutto, usa il mortaio o il frullatore a intermittenza, aggiungi subito l'olio che protegge il basilico dall'ossigeno, e conserva sempre con uno strato di olio in superficie."),
      ("Posso sostituire i pinoli?", "Le noci sono il sostituto più usato — più economiche e facilmente reperibili. Mandorle pelate o anacardi danno una versione neutra e meno dolce. I pistacchi di Bronte creano un pesto al pistacchio delizioso ma diverso dall'originale. Il sapore cambia ma il risultato è sempre buono."),
      ("Con quale pasta si serve il pesto genovese?", "Le trofie liguri sono la scelta tradizionale — la loro forma attorcigliata cattura perfettamente il pesto. Le trenette (tagliatelle liguri più strette) sono l'alternativa classica. Gli spaghetti e i linguine funzionano bene. La pasta al pesto autentica ligure include anche patate a dadini e fagiolini cotti nella stessa acqua della pasta."),
      ("Quanto sale aggiungere?", "Il sale va aggiunto molto con parsimonia perché il Parmigiano, il Pecorino e i pinoli contengono già sale naturale. Assaggia sempre prima di salare. Il pizzico di sale grosso nel primo passaggio con l'aglio serve come abrasivo per facilitare la pestatura, non come condimento principale."),
    ],
  },

  # ─── 20 — supplì romani ──────────────────────────────────
  {
    "slug":        "suppli-romani-ricetta",
    "title":       "Supplì Romani Ricetta Originale — Il Street Food di Roma al Telefono",
    "desc":        "La ricetta originale dei supplì romani: riso al ragù, mozzarella filante, impanatura croccante. Il vero street food romano al telefono fatto in casa.",
    "tag":         "Antipasti",
    "tag_color":   "#e65100",
    "tag_bg":      "#fff3e0",
    "h1":          "Supplì Romani Ricetta Originale — Il Re dello Street Food di Roma",
    "intro":       "I supplì romani sono il re indiscusso dello street food di Roma. Diversi dagli arancini siciliani per forma (ovali e allungati), per il ripieno (ragù di carne e mozzarella), e per l'impanatura (doppia panatura con uovo e pangrattato), i supplì romani hanno un nome tutto loro: 'al telefono' — perché quando li si spezza a metà, la mozzarella fonde crea un filo lunghissimo simile al filo del telefono. Una friggitoria senza supplì a Roma non è una vera friggitoria.",
    "prep":        "30 min", "cook": "1h", "total": "1h 30min",
    "servings":    "12 supplì", "calories": "~220", "difficulty": "Medio",
    "badge_text":  "Street Food",
    "cuisine":     "Italiana",
    "category":    "Antipasti",
    "keywords":    "supplì romani ricetta originale, supplì al telefono ricetta, supplì romani ricetta, suppli romani come fare, street food romano supplì",
    "cal_num":     "220", "protein": "9g", "fat": "10g", "carbs": "24g",
    "ingredients": [
      "300g riso Roma o Carnaroli",
      "200g carne macinata mista (metà manzo, metà maiale)",
      "200g passata di pomodoro",
      "1 cipolla piccola",
      "50ml vino rosso",
      "200g mozzarella fiordilatte (tagliata a cubetti e asciugata bene)",
      "50g Parmigiano Reggiano grattugiato",
      "2 uova grandi",
      "150g pangrattato fine",
      "Olio di semi di arachide abbondante (per friggere)",
      "Sale, pepe e olio extravergine q.b.",
    ],
    "steps": [
      "Prepara il ragù: soffriggi la cipolla tritata finemente in 2 cucchiai di olio per 5 minuti. Aggiungi la carne macinata e rosolala a fuoco alto fino a doratura completa, rompendola bene con un cucchiaio. Aggiungi il vino rosso, lascia sfumare completamente. Aggiungi la passata di pomodoro, sala, pepa e cuoci a fuoco basso per 30 minuti fino ad avere un ragù denso e asciutto.",
      "Cuoci il riso: porta a ebollizione 600ml di acqua salata. Aggiungi il riso e cuoci assorbendo tutta l'acqua come un risotto (circa 16-18 minuti). Spegni, aggiungi il Parmigiano e mescola bene. Lascia intiepidire 10 minuti.",
      "Unisci il riso intiepidito al ragù. Mescola accuratamente fino ad avere un composto omogeneo, denso e lavorabile con le mani. Lascia raffreddare completamente — almeno 1 ora a temperatura ambiente o 30 minuti in frigorifero.",
      "Forma i supplì: bagna le mani con acqua fredda. Prendi una porzione di riso (circa 80g) e appiattiscila nel palmo della mano. Posiziona 1-2 cubetti di mozzarella al centro. Chiudi il riso intorno alla mozzarella formando una polpetta ovale e allungata, simile a un uovo grande. Premi bene per compattare.",
      "Doppia panatura: passa ogni supplì prima nella farina, poi nell'uovo sbattuto, poi nel pangrattato. Ripeti il passaggio nell'uovo e nel pangrattato una seconda volta per una panatura più spessa e croccante.",
      "Friggi: scalda l'olio di arachide in una pentola alta a 175-180°C. Friggi i supplì in piccole riprese (3-4 per volta) per 4-5 minuti, girandoli delicatamente, fino a doratura intensa e uniforme su tutti i lati.",
      "Scola su carta assorbente e sala leggermente. Servi immediatamente — i supplì devono essere mangiati caldi per godersi il cuore filante di mozzarella.",
    ],
    "tips": [
      "Il riso deve essere completamente freddo prima di formare i supplì: caldo si attacca alle mani e non mantiene la forma.",
      "La mozzarella deve essere ASCIUTTA: tagliala il giorno prima e lasciala su carta assorbente in frigorifero per eliminare il siero in eccesso.",
      "La doppia panatura è fondamentale: crea la crosta croccante che non si spacca durante la frittura.",
      "Non sovraffollare la padella: abbassa la temperatura dell'olio e i supplì assorbiranno troppo olio invece di cuocere.",
    ],
    "prose1_h2":  "I Supplì vs gli Arancini: La Rivalità Secolare tra Roma e Palermo",
    "prose1":     """La rivalità tra supplì romani e arancini siciliani è una delle più sentite e animate della gastronomia italiana. Entrambi sono polpette di riso impanate e fritte. Ma le differenze sono profonde e i rispettivi sostenitori le difendono con passione quasi religiosa. I supplì romani sono ovali e allungati, ripieni di ragù di carne e mozzarella filante, con riso cotto nel ragù stesso. Gli arancini siciliani sono sferici (a Catania conici), ripieni di ragù, piselli e tuma o di prosciutto e besciamella, con riso allo zafferano. I supplì si mangiano come street food in piedi, bollenti, appena fritti. Gli arancini sono più elaborati e spesso accompagnano aperitivi. La parola 'supplì' deriverebbe dal francese 'surprise' — la sorpresa è il cuore filante di mozzarella. A Roma, chiedere un arancino invece di un supplì è ancora oggi una gaffe diplomatica.""",
    "prose2_h2":  "La Mozzarella 'al Telefono': Il Segreto del Cuore Filante",
    "prose2":     """Il soprannome 'al telefono' definisce la caratteristica più spettacolare e desiderata del supplì romano: quando lo spezzi a metà, la mozzarella fusa crea un filo lunghissimo e lucido tra le due metà — come il filo dell'antico telefono a cornetta. Per ottenere questo effetto perfetto, la mozzarella deve essere fiordilatte (non bufala, troppo acquosa) tagliata a cubetti e asciugata perfettamente dal siero il giorno prima. La mozzarella deve essere al centro esatto del supplì, completamente avvolta dal riso su tutti i lati, senza spazi vuoti che potrebbero far fuoriuscire il formaggio durante la frittura. La temperatura dell'olio deve essere corretta: a 180°C la mozzarella si fonde lentamente durante i 4-5 minuti di frittura creando il cuore filante; a temperatura più bassa si scioglie troppo e fuoriesce; a temperatura più alta la panatura brucia prima che la mozzarella si fondi.""",
    "img2_alt":   "Supplì romano spezzato a metà con il cuore filante di mozzarella che crea il classico 'filo del telefono'",
    "prose3_h2":  "Conservazione, Frittura Perfetta e le Varianti Moderne",
    "prose3":     """I supplì si possono preparare in anticipo fino al momento della panatura e conservare in frigorifero per 24 ore, oppure congelati (panati ma non fritti) per 2 mesi — friggi direttamente da congelato aggiungendo 2 minuti in più. I supplì fritti si conservano male: la panatura si ammorbidisce rapidamente. Mangiati freddi perdono il loro fascino. Tra le varianti romane moderne più creative: supplì alla cacio e pepe (riso mantecato con Pecorino e pepe invece del ragù), alla carbonara (riso con guanciale, uovo e Pecorino), alla amatriciana, e la versione vegetariana con zucchine e ricotta. Tutte rispettano la forma ovale e la doppia panatura croccante che è il marchio identitario del supplì romano.""",
    "faqs": [
      ("Qual è la differenza tra supplì e arancini?", "I supplì romani sono ovali e allungati, ripieni di ragù di carne e mozzarella filante, con riso cotto nel ragù. Gli arancini siciliani sono rotondi (o conici a Catania), con riso allo zafferano e diversi ripieni (ragù+piselli, prosciutto+besciamella). Due piatti distinti con identità regionale propria — non intercambiabili."),
      ("Posso usare il riso avanzato?", "Sì — il riso avanzato del giorno prima, già freddo, è perfetto per i supplì. Mescola con il ragù freddo e procedi con la formatura. Il riso freddo è anzi più facile da lavorare di quello appena cotto."),
      ("Perché i miei supplì si aprono durante la frittura?", "Tre possibili cause: la panatura non è abbastanza spessa (fai sempre la doppia panatura), il riso era ancora caldo quando hai formato i supplì (deve essere completamente freddo), oppure la mozzarella non era abbastanza asciutta e ha rilasciato acqua durante la cottura."),
      ("Posso cuocerli al forno invece di friggerli?", "Sì ma il risultato è molto diverso: la panatura rimane opaca e meno croccante. Se vuoi provarci: spennella con olio e cuoci a 200°C per 20-25 minuti girando a metà cottura. Il cuore di mozzarella si fonderà comunque. Ma la vera crosta del supplì romano si ottiene solo con la frittura in olio abbondante."),
      ("Quale tipo di riso usare?", "Il riso Roma o il Carnaroli sono i migliori: rilasciano amido durante la cottura creando una consistenza collosa che tiene insieme il supplì. Il riso Arborio funziona bene. Evita il riso parboiled o il riso a chicco lungo: sono troppo sgranati e il supplì non manterrà la forma."),
    ],
  },

  # ─── 21 — cantucci toscani ───────────────────────────────
  {
    "slug":        "cantucci-toscani-ricetta",
    "title":       "Cantucci Toscani Ricetta Originale — I Biscotti di Prato alle Mandorle",
    "desc":        "La ricetta originale dei cantucci toscani di Prato: mandorle intere tostate, uova, farina e zucchero. Croccanti, profumati e perfetti inzuppati nel Vin Santo.",
    "tag":         "Dolci",
    "tag_color":   "#6a1b9a",
    "tag_bg":      "#f3e5f5",
    "h1":          "Cantucci Toscani Ricetta Originale — I Biscotti di Prato alle Mandorle",
    "intro":       "I cantucci toscani — chiamati anche 'biscotti di Prato' — sono i biscotti più famosi della Toscana e tra i più imitati al mondo. Duri, croccanti, profumati di mandorle tostate e scorza d'arancia, sono pensati per essere inzuppati nel Vin Santo DOC — il vino da dessert toscano per eccellenza. La ricetta originale del pasticcere pratese Antonio Mattei, depositata nel 1858, è rimasta praticamente invariata: farina, zucchero, uova, mandorle intere non pelate, e nient'altro. Niente burro, niente lievito chimico. Solo la semplicità della tradizione.",
    "prep":        "20 min", "cook": "35 min", "total": "55 min",
    "servings":    "35 cantucci", "calories": "~85", "difficulty": "Facile",
    "badge_text":  "Toscani",
    "cuisine":     "Italiana",
    "category":    "Dolci",
    "keywords":    "cantucci toscani ricetta originale, cantucci alle mandorle ricetta, biscotti di prato ricetta, cantucci toscani ricetta della nonna, come fare i cantucci",
    "cal_num":     "85", "protein": "2g", "fat": "3g", "carbs": "12g",
    "ingredients": [
      "300g farina 00",
      "200g zucchero semolato",
      "200g mandorle intere non pelate (con la buccia)",
      "3 uova grandi a temperatura ambiente",
      "1 cucchiaino di estratto naturale di vaniglia",
      "Scorza grattugiata di 1 arancia non trattata",
      "1 cucchiaino di lievito per dolci",
      "1 pizzico di sale",
      "1 tuorlo d'uovo + 1 cucchiaio di latte (per la doratura)",
    ],
    "steps": [
      "Preriscalda il forno a 180°C statico. Tosta le mandorle intere in una padella asciutta a fuoco medio per 5-6 minuti mescolando spesso, fino a che profumano e la buccia inizia a scurirsi leggermente. Tostate, le mandorle diventano più croccanti e aromatiche. Lascia raffreddare completamente.",
      "In una ciotola capiente, mescola la farina setacciata con lo zucchero, il lievito e il sale. Aggiungi la scorza d'arancia grattugiata e la vaniglia.",
      "Sbatti le 3 uova intere e aggiungile alla farina. Mescola prima con una forchetta, poi con le mani fino a ottenere un impasto compatto, omogeneo e leggermente appiccicoso — simile alla pasta frolla.",
      "Incorpora le mandorle tostate intere nell'impasto, distribuendole uniformemente.",
      "Dividi l'impasto in 2 parti uguali. Su una superficie leggermente infarinata, forma due filoni lunghi circa 25cm, larghi 5cm e alti 3cm. Sistemarli distanziati su una teglia rivestita di carta forno.",
      "Spennella la superficie dei filoni con il tuorlo sbattuto con il latte. Inforna a 180°C per 25 minuti fino a doratura dorata uniforme — i filoni devono essere sodi al tatto.",
      "Sforna i filoni e lascia riposare 5 minuti. Taglia in diagonale a fette di 1,5-2cm con un coltello affilato e deciso. Rimetti i cantucci tagliati sulla teglia con il lato del taglio verso l'alto. Riinforna a 160°C per altri 10-12 minuti per asciugarli e renderli croccanti. Lascia raffreddare completamente su una griglia prima di servire.",
    ],
    "tips": [
      "Le mandorle non pelate sono fondamentali nell'originale di Prato: la buccia aggiunge sapore e croccantezza.",
      "Taglia i filoni mentre sono ancora caldi ma non bollenti: troppo caldi si sbriciola, troppo freddi si rompono.",
      "Il secondo passaggio in forno (biscottatura) è ciò che li rende croccanti: non saltarlo mai.",
      "Conserva in una scatola di latta: durano fino a 4 settimane mantenendo la croccantezza perfetta.",
    ],
    "prose1_h2":  "Da Prato al Mondo: La Storia dei Cantucci di Antonio Mattei",
    "prose1":     """La storia dei cantucci toscani è legata indissolubilmente a Prato e alla famiglia Mattei. Nel 1858, il pasticcere pratese Antonio Mattei aprì la sua pasticceria in Via Ricasoli a Prato e iniziò a produrre i 'biscotti di Prato' secondo una ricetta che sosteneva fosse di origine rinascimentale. I suoi biscotti vinsero la medaglia d'argento all'Esposizione di Firenze del 1861, appena un anno dopo l'Unità d'Italia, e poi premi a Londra e Parigi. La pasticceria Mattei esiste ancora oggi, in via Ricasoli, e produce cantucci con la stessa ricetta originale di oltre 160 anni fa. Il nome 'cantuccio' deriva probabilmente da 'canto' (angolo, spigolo) — il riferimento alla forma spigolosa del biscotto tagliato in diagonale. La tradizione vuole che i cantucci vengano serviti alla fine del pasto con un piccolo bicchiere di Vin Santo DOC toscano nel quale inzupparli.""",
    "prose2_h2":  "Cantucci vs Biscotti: La Confusione Internazionale e la Verità Toscana",
    "prose2":     """Nel mondo anglosassone, tutti i biscotti italiani a doppia cottura vengono chiamati genericamente 'biscotti' — termine che in italiano significa semplicemente 'cotto due volte' (bis-cotto). In Toscana, questi specifici biscotti alle mandorle di Prato si chiamano 'cantucci' o 'biscotti di Prato', mai semplicemente 'biscotti'. La doppia cottura (prima il filone intero, poi le fette) è il metodo che li rende così duri e croccanti — e quindi perfetti per l'inzuppo nel Vin Santo senza sfaldarsi. La ricetta originale di Mattei non include burro (a differenza di molte versioni commerciali moderne), né lievito chimico nella versione più tradizionale. Le mandorle devono essere intere e non pelate — un dettaglio spesso ignorato nelle imitazioni internazionali che usano mandorle pelate o a scaglie.""",
    "img2_alt":   "Cantucci toscani dorati in un sacchetto di carta kraft con un bicchiere di Vin Santo toscano accanto",
    "prose3_h2":  "Conservazione, Varianti e l'Abbinamento con il Vin Santo",
    "prose3":     """I cantucci toscani sono uno dei dolci italiani che si conserva meglio: in una scatola di latta o in un contenitore ermetico durano facilmente 3-4 settimane senza perdere croccantezza. Anzi, migliorano con il tempo — gli aromi delle mandorle tostate e dell'arancia si intensificano. Tra le varianti più diffuse: cantucci al pistacchio (con pistacchi di Bronte in sostituzione delle mandorle), al cioccolato fondente (con gocce di cioccolato nell'impasto), alla nocciola, e la versione moderna 'morbida' (con più burro e cottura singola) — quest'ultima però non è la ricetta tradizionale di Prato. L'abbinamento classico con il Vin Santo DOC toscano è un'esperienza gastronomica unica: il Vin Santo ambrato, dolce e leggermente ossidato, con le sue note di miele e albicocca secca, contrasta e completa perfettamente la croccantezza e il profumo di mandorle dei cantucci.""",
    "faqs": [
      ("Perché i miei cantucci si sono sbriciolati quando li ho tagliati?", "Il filone era troppo freddo al momento del taglio. I cantucci vanno tagliati quando sono ancora caldi (5-10 minuti dopo la prima sfornata) ma non bollenti. Usa un coltello a lama liscia e affilata con un movimento deciso e verticale — non segare avanti e indietro."),
      ("Posso omettere le mandorle o sostituirle?", "La ricetta originale di Prato richiede mandorle intere con la buccia: sono l'ingrediente identitario. Puoi sostituirle con pistacchi, nocciole o noci per varianti moderne. Per versioni senza frutta secca, aggiungi gocce di cioccolato fondente o scorze d'arancia candite."),
      ("Con cosa si servono i cantucci se non ho il Vin Santo?", "Qualsiasi vino da dessert dolce funziona bene: il Passito di Pantelleria, il Moscato d'Asti, il Marsala vergine. Fuori dall'Italia, il Porto vintage è un abbinamento eccellente. Per una versione analcolica, inzuppali nel caffè espresso o nel tè nero forte."),
      ("Perché i miei cantucci non sono croccanti?", "Il secondo passaggio in forno (la biscottatura) non è durato abbastanza. I cantucci devono essere completamente asciutti e secchi: il colore del taglio deve essere giallo chiaro, non ancora umido al centro. Rimetti in forno per altri 5-7 minuti a 160°C. Lascia raffreddare completamente su una griglia prima di chiuderli: si induriscono ulteriormente raffreddandosi."),
      ("Posso aggiungere il burro all'impasto?", "La ricetta originale di Antonio Mattei non prevede burro — la durezza e croccantezza caratteristica dei cantucci dipende proprio dall'assenza di grassi aggiunti. Con il burro, i cantucci diventano più morbidi e si conservano meno. Alcune versioni moderne aggiungono 50g di burro per un risultato più friabile: è una scelta gustosa ma non tradizionale."),
    ],
  },

  # ─── 22 — lasagne alla bolognese ────────────────────────
  {
    "slug":        "lasagne-alla-bolognese-ricetta",
    "title":       "Lasagne al Forno Ricetta Originale Bolognese — La Vera Lasagna della Tradizione",
    "desc":        "La vera ricetta delle lasagne al forno bolognesi: ragù di carne lento, besciamella vellutata, sfoglie fresche e Parmigiano Reggiano. La ricetta originale dell'Accademia Italiana della Cucina.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Lasagne al Forno Ricetta Originale Bolognese — La Vera Ricetta della Tradizione",
    "intro":       "Le lasagne al forno alla bolognese sono forse il piatto più rappresentativo della cucina italiana nel mondo. Eppure spesso vengono preparate male: ragù troppo veloce, besciamella grumosa, sfoglie secche che rimangono dure. La ricetta autentica registrata dall'Accademia Italiana della Cucina prevede un ragù di carne misto cotto per almeno 2 ore, una besciamella vellutata preparata con il roux classico, sfoglie di pasta all'uovo e abbondante Parmigiano Reggiano DOP a ogni strato. Il risultato è un primo piatto sontuoso, ricco, profumato — la domenica italiana per eccellenza.",
    "prep":        "45 min", "cook": "2h 30min", "total": "3h 15min",
    "servings":    "8 porzioni", "calories": "~520", "difficulty": "Medio",
    "badge_text":  "Domenica",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "lasagne al forno ricetta originale bolognese, lasagne alla bolognese, ricetta lasagne, lasagne al forno, lasagna bolognese ricetta originale",
    "cal_num":     "520", "protein": "32g", "fat": "28g", "carbs": "44g",
    "ingredients": [
      "400g macinato di manzo (almeno 15-20% di grasso)",
      "200g macinato di maiale",
      "150g pancetta tesa non affumicata, a cubetti piccoli",
      "1 cipolla dorata grande, tritata finemente",
      "2 carote medie, tritate finemente",
      "2 gambi di sedano, tritati finemente",
      "2 cucchiai di concentrato di pomodoro",
      "200ml vino rosso secco (Sangiovese o Chianti)",
      "400ml latte intero",
      "2 cucchiai di olio extravergine d'oliva",
      "1 litro di latte intero (per la besciamella)",
      "80g di burro (per la besciamella)",
      "80g di farina 00 (per la besciamella)",
      "1/2 cucchiaino di noce moscata grattugiata",
      "500g sfoglie di lasagna fresca all'uovo (o 300g lasagne secche precotte)",
      "100g Parmigiano Reggiano DOP grattugiato",
      "30g burro a fiocchetti per la superficie",
      "Sale e pepe nero q.b.",
    ],
    "steps": [
      "Prepara il soffritto: in una casseruola larga, scalda l'olio a fuoco medio. Aggiungi la pancetta e rosola 3-4 minuti finché il grasso si scioglie. Aggiungi cipolla, carota e sedano e cuoci lentamente per 10-12 minuti finché le verdure sono morbide e appassite. Questo soffritto è il cuore del ragù.",
      "Aggiungi i macinati di manzo e maiale. Alza la fiamma e rosola rompendo i grumi con un cucchiaio di legno, finché la carne è ben dorata e non più rosa — circa 10 minuti. Non affrettare: la rosolatura crea il sapore.",
      "Aggiungi il vino rosso tutto in una volta. Lascia sfumare a fuoco vivo per 2-3 minuti finché l'alcol è completamente evaporato.",
      "Aggiungi il concentrato di pomodoro, mescola bene. Poi aggiungi il latte intero. Copri parzialmente con un coperchio e abbassa la fiamma al minimo. Cuoci per almeno 2 ore, mescolando ogni 20-30 minuti. Il ragù è pronto quando è denso, cremoso, con il grasso che affiora in superficie.",
      "Prepara la besciamella: scioglii il burro in un tegame a fuoco medio. Aggiungi la farina tutta in una volta e mescola con una frusta per 2 minuti (roux dorato). Aggiungi il latte caldo poco alla volta, mescolando continuamente. Cuoci 5-7 minuti finché la besciamella si addensa. Aggiusta di sale e noce moscata.",
      "Preriscalda il forno a 180°C statico. Imburra generosamente una teglia da 30x20cm. Stendi un primo strato sottile di besciamella sul fondo per evitare che le sfoglie attacchino.",
      "Assembla le lasagne: strati alternati di sfoglie di pasta, ragù bolognese, besciamella e Parmigiano Reggiano. Ripeti per almeno 5-6 strati. Sull'ultimo strato: besciamella abbondante, Parmigiano generoso e fiocchetti di burro.",
      "Copri con carta stagnola e inforna per 30 minuti. Rimuovi la stagnola e cuoci altri 15-20 minuti finché la superficie è dorata e gratinata. Lascia riposare 10 minuti prima di servire — fondamentale per compattare gli strati.",
    ],
    "tips": [
      "Il ragù deve cuocere almeno 2 ore: sotto le 2 ore il collagene non si scioglie e il ragù resta granulare.",
      "Usa latte intero nel ragù (non brodo): è la scelta originale bolognese e rende la carne cremosa.",
      "La besciamella deve essere più morbida del solito: si asciuga in forno, quindi preparala leggermente più liquida.",
      "Lascia riposare 10 minuti dopo il forno: le lasagne calde sono liquide, dopo 10 minuti si tagliano perfettamente.",
    ],
    "prose1_h2":  "L'Origine della Vera Lasagna Bolognese: La Ricetta Depositata nel 1982",
    "prose1":     """La ricetta autentica delle lasagne alla bolognese è stata depositata ufficialmente nel 1982 dall'Accademia Italiana della Cucina presso la Camera di Commercio di Bologna. La ricetta originale prevede sfoglie di pasta all'uovo verde (con spinaci) e un ragù che non include il pomodoro pelato — solo concentrato — contrariamente a molte versioni popolari. Il latte intero nel ragù è la firma del ragù bolognese autentico, che lo distingue da tutti gli altri ragù italiani. A Bologna, le lasagne sono il piatto della domenica per eccellenza: ogni famiglia ha la propria versione, tramandata di nonna in nonna, con piccole variazioni che ne fanno un patrimonio familiare irripetibile.""",
    "prose2_h2":  "Besciamella o Mozzarella? La Grande Divisione tra Nord e Sud Italia",
    "prose2":     """Nel Sud Italia (Campania, Sicilia) le lasagne si preparano tradizionalmente con mozzarella, uova sode, ricotta e salame — niente besciamella. Al Nord (Emilia-Romagna, Lombardia, Piemonte) la besciamella è obbligatoria. Nessuna delle due è sbagliata: sono due tradizioni regionali diverse e ugualmente autentiche. La versione bolognese con besciamella è quella più conosciuta nel mondo e quella registrata ufficialmente dall'Accademia. La besciamella crea una cremosità avvolgente che si amalgama con il ragù in modo irripetibile — un abbraccio caldo in ogni forchettata.""",
    "img2_alt":   "Lasagne al forno bolognesi tagliate nella teglia mostrando gli strati di ragù, besciamella dorata e Parmigiano gratinato",
    "prose3_h2":  "Conservazione, Congelamento e il Segreto del Giorno Dopo",
    "prose3":     """Le lasagne al forno si conservano in frigorifero per 3-4 giorni coperte con pellicola. Il sapore migliora il giorno dopo — è uno dei rari piatti che il giorno dopo è ancora più buono: gli strati si compattano, i sapori si amalgamano e le lasagne si tagliano perfettamente. Per congelare: porziona le lasagne fredde, avvolgi ogni porzione in carta stagnola e conserva in freezer fino a 3 mesi. Per riscaldare dal congelato: in forno a 160°C coperto per 30 minuti, poi scoperto per 10 minuti. Le lasagne avanzate sono perfette anche scaldate in padella con un filo d'acqua e coperte con un coperchio.""",
    "faqs": [
      ("Posso usare lasagne secche invece di fresche?", "Sì — le lasagne secche precotte funzionano bene. Non richiedono precottura: l'umidità della besciamella e del ragù le cuoce durante la cottura in forno. Usa una besciamella leggermente più liquida del normale per garantire che le sfoglie si cuociano bene. Le lasagne fresche danno un risultato più delicato e setoso — se hai tempo, preparale in casa."),
      ("Quanti strati dovrebbero avere le lasagne?", "Almeno 5-6 strati. Sotto i 5 strati le lasagne sono troppo sottili e si seccano. 6-8 strati è il range ideale per una teglia da 30x20cm. L'importante è che ogni strato sia uniforme e che l'ultimo strato sia generosamente coperto di besciamella per creare la crosticina gratinata che è la firma delle lasagne al forno perfette."),
      ("Il ragù può cuocere meno di 2 ore?", "Tecnicamente sì, ma il risultato sarà molto diverso. Sotto le 2 ore il ragù è ancora granulare e asciutto. Dopo 2 ore il collagene della carne si scioglie e il ragù diventa cremoso e avvolgente. Se hai fretta, usa una pentola a pressione: 45 minuti a pressione equivalgono a circa 2 ore di cottura tradizionale."),
      ("La lasagna si può preparare il giorno prima?", "Assolutamente sì — è anzi consigliato. Assembla le lasagne il giorno prima, copri con pellicola e conserva in frigorifero. Inforna direttamente dal freddo: aggiungi 10-15 minuti al tempo di cottura. Il sapore sarà ancora migliore: gli strati si compattano e i sapori si amalgamano durante la notte."),
      ("Perché la mia besciamella è grumosa?", "I grumi si formano quando si aggiunge il latte troppo velocemente o troppo freddo. Aggiungilo sempre caldo e poco alla volta, mescolando continuamente con una frusta. Se si formano dei grumi, non preoccuparti: passa la besciamella al minipimer per 30 secondi e tornerà liscia e vellutata."),
    ],
  },

  # ─── 23 — risotto alla milanese ──────────────────────────
  {
    "slug":        "risotto-alla-milanese-ricetta",
    "title":       "Risotto alla Milanese Ricetta Originale — Il Risotto con lo Zafferano di Milano",
    "desc":        "Il vero risotto alla milanese: Carnaroli, brodo di carne, zafferano DOP e mantecatura con burro e Parmigiano. La ricetta originale del risotto giallo milanese passo per passo.",
    "tag":         "Secondi",
    "tag_color":   "#c62828",
    "tag_bg":      "#ffebee",
    "h1":          "Risotto alla Milanese Ricetta Originale — Il Risotto Giallo con lo Zafferano",
    "intro":       "Il risotto alla milanese — o 'risotto giallo' — è il piatto simbolo di Milano. Cremoso, giallo intenso grazie allo zafferano di qualità, con una mantecatura ricca di burro e Parmigiano Reggiano che lo rende vellutato e avvolgente. La chiave del risotto perfetto non è la ricetta, ma la tecnica: il tostare il riso a secco, il brodo aggiunto bollente mestolo per mestolo, e la mantecatura fuori dal fuoco con burro freddo. Tre passi, un capolavoro.",
    "prep":        "10 min", "cook": "25 min", "total": "35 min",
    "servings":    "4 porzioni", "calories": "~480", "difficulty": "Medio",
    "badge_text":  "Milanese",
    "cuisine":     "Italiana",
    "category":    "Secondi",
    "keywords":    "risotto alla milanese ricetta originale, risotto allo zafferano, risotto giallo milanese, risotto milanese con zafferano, come fare il risotto alla milanese",
    "cal_num":     "480", "protein": "14g", "fat": "22g", "carbs": "58g",
    "ingredients": [
      "320g riso Carnaroli (o Vialone Nano)",
      "1.5L brodo di carne caldo (manzo + pollo)",
      "1 bustina (0.15g) zafferano DOP in pistilli o polvere",
      "1 scalogno piccolo, tritato finissimo",
      "80g burro freddo, diviso in 40g + 40g",
      "100ml vino bianco secco",
      "80g Parmigiano Reggiano DOP, grattugiato fresco",
      "30g midollo di bue (opzionale ma tradizionale)",
      "Sale q.b.",
    ],
    "steps": [
      "Scalda il brodo di carne fino a leggero bollore e mantienilo caldo per tutta la cottura — il brodo freddo blocca la cottura del riso e rompe la cremosità.",
      "Sciogli lo zafferano in un mestolo di brodo caldo. Lascialo in infusione per almeno 15 minuti — il colore e il profumo si intensificano con il riposo.",
      "In una casseruola larga, scioglii 40g di burro a fuoco medio. Aggiungi lo scalogno (e il midollo se lo usi) e cuoci dolcemente per 3-4 minuti finché è trasparente. Non deve colorire.",
      "Aggiungi il riso Carnaroli e tosta a fuoco vivo per 2-3 minuti, mescolando costantemente, finché i chicchi sono traslucidi ai bordi e si sente uno sfrigolio secco. La tostatura impermeabilizza il riso.",
      "Sfuma con il vino bianco. Mescola finché l'alcol è completamente evaporato — circa 1 minuto a fuoco vivo.",
      "Aggiungi il brodo allo zafferano. Da questo momento, aggiungi il brodo caldo un mestolo alla volta, mescolando e aspettando che ogni aggiunta sia quasi assorbita prima di aggiungere la successiva. Continua per 16-18 minuti totali.",
      "Spegni il fuoco quando il riso è al dente e il risotto ha ancora una consistenza fluida — deve 'scorrere' leggermente. Toglilo dal fuoco un minuto prima di quanto sembri pronto.",
      "Mantecatura: aggiungi i restanti 40g di burro freddo a cubetti e il Parmigiano grattugiato. Mescola vigorosamente fuori dal fuoco per 1-2 minuti. Il risotto deve diventare lucido, cremoso, vellutato. Servi immediatamente.",
    ],
    "tips": [
      "Il brodo deve essere caldissimo per tutta la cottura: un mestolo freddo blocca la cottura e rompe la cremosità.",
      "Non lavare mai il riso: l'amido in superficie è quello che crea la cremosità del risotto.",
      "La mantecatura fuori dal fuoco è fondamentale: il burro freddo si emulsiona senza sciogliersi.",
      "Usa pistilli di zafferano DOP se li trovi: il colore e il profumo sono superiori alla polvere.",
    ],
    "prose1_h2":  "La Leggenda dello Zafferano: Come Nacque il Risotto Giallo di Milano",
    "prose1":     """La leggenda vuole che il risotto alla milanese sia nato nel 1574 durante i lavori del Duomo di Milano. Un giovane apprendista del mastro vetraio — soprannominato 'Zafferano' per il suo uso eccessivo della preziosa spezia nelle vetrate — avrebbe aggiunto per scherzo dello zafferano al risotto servito al banchetto nuziale. Il risultato fu così gradito che il piatto rimase nella tradizione milanese per sempre. La realtà storica è altrettanto affascinante: l'uso dello zafferano in cucina a Milano è documentato già nel Rinascimento, quando la spezia arrivava via Venezia dalle rotte commerciali con il Medio Oriente. Oggi lo zafferano dell'Aquila — il più pregiato al mondo — è la scelta dei puristi.""",
    "prose2_h2":  "Carnaroli, Vialone Nano o Arborio: Quale Riso Scegliere per il Risotto Perfetto?",
    "prose2":     """Il Carnaroli è il re del risotto milanese: i suoi chicchi grandi tengono perfettamente la cottura, rilasciano amido gradualmente per la cremosità, e reggono la mantecatura vigorosa. Il Vialone Nano è la scelta veneta — più piccolo, più amidoso, risultato leggermente più morbido. L'Arborio è il più diffuso ma il meno pregiato: i chicchi si rompono facilmente e il risotto tende a diventare colloso. Se vuoi il risotto milanese perfetto, usa sempre il Carnaroli senza esitazione.""",
    "img2_alt":   "Risotto alla milanese giallo intenso allo zafferano cremoso e lucido nel piatto fondo bianco con Parmigiano grattugiato",
    "prose3_h2":  "Il Segreto della Mantecatura Perfetta: Burro Freddo e Movimento Deciso",
    "prose3":     """La mantecatura è l'operazione più delicata e più importante del risotto. Consiste nell'aggiungere burro freddo (e Parmigiano) fuori dal fuoco e mescolare vigorosamente per emulsionare i grassi nell'amido del riso. Il burro deve essere freddo da frigorifero: il burro caldo si scioglie subito senza emulsionarsi e il risotto risulta oleoso invece che cremoso. Il movimento giusto è un colpo di polso deciso, quasi a 'sbattere' il risotto contro i bordi della casseruola. Il risultato è un risotto lucido, vellutato, che scorre all'onda ma non è liquido. Va servito entro 2-3 minuti dalla mantecatura — il risotto non attende nessuno.""",
    "faqs": [
      ("Posso usare il brodo di dado invece del brodo fatto in casa?", "Sì, ma il sapore sarà meno ricco e più salato. Se usi il dado, scegli uno di qualità biologico senza glutammato e assaggia prima di aggiungere sale. Il brodo fatto in casa con ossobuco e verdure dà un risotto dal sapore nettamente superiore. Se hai tempo, prepara il brodo il giorno prima."),
      ("Perché il mio risotto è appiccicoso?", "Il risotto appiccicoso si ottiene quando si mescola troppo continuamente, quando il riso viene lavato (perdendo l'amido naturale) o quando si usa Arborio. Mescola con regolarità ma non ossessivamente. Usa Carnaroli per un risultato al dente e non gommoso."),
      ("Posso preparare il risotto in anticipo?", "Il risotto non si prepara in anticipo — perde completamente la texture. Esiste però la tecnica della cottura interrotta: cuoci il risotto per 3/4 del tempo, stendilo su una teglia fredda per bloccarne la cottura, e finisci la cottura con l'ultimo brodo e la mantecatura solo al momento di servire. È la tecnica usata dai ristoranti."),
      ("Come si scalda il risotto avanzato?", "Metti il risotto freddo in padella con un mestolo di brodo caldo. Scalda a fuoco medio mescolando energicamente finché torna caldo e cremoso. Aggiungi una noce di burro e una spolverata di Parmigiano. Non scaldare mai al microonde: asciuga il riso e lo rende gommoso."),
      ("Quanti pistilli di zafferano devo usare?", "La dose standard è 0.15g (una bustina di polvere o circa 20-25 pistilli) per 4 porzioni. I pistilli danno un colore più profondo e un profumo più complesso della polvere. Per un colore più intenso puoi arrivare a 0.25g. Lo zafferano DOP dell'Aquila è considerato il migliore al mondo per intensità aromatica."),
    ],
  },

  # ─── 24 — polpette al sugo ────────────────────────────────
  {
    "slug":        "polpette-al-sugo-ricetta",
    "title":       "Polpette al Sugo Ricetta della Nonna Originale — Morbide e Saporite come un Tempo",
    "desc":        "Le polpette al sugo della nonna: carne mista, pane ammollato nel latte, uova e prezzemolo in un sugo di pomodoro denso. La ricetta originale italiana per polpette morbide che si sciolgono in bocca.",
    "tag":         "Secondi",
    "tag_color":   "#c62828",
    "tag_bg":      "#ffebee",
    "h1":          "Polpette al Sugo Ricetta della Nonna — Morbide come un Tempo",
    "intro":       "Le polpette al sugo sono il piatto della domenica per eccellenza, quello che profuma tutta la casa fin dal mattino. Ogni nonna italiana ha la sua versione — ma i segreti sono sempre gli stessi: carne mista (non solo manzo), pane raffermo ammollato nel latte (non pangrattato), uova per legare, e un sugo di pomodoro denso e profumato nel quale le polpette terminano la cottura. Il risultato sono polpette morbide, succose, che si sciolgono letteralmente in bocca — impossibili da ottenere con le polpette cotte solo in padella o al forno.",
    "prep":        "25 min", "cook": "45 min", "total": "1h 10min",
    "servings":    "4 porzioni", "calories": "~420", "difficulty": "Facile",
    "badge_text":  "Domenica",
    "cuisine":     "Italiana",
    "category":    "Secondi",
    "keywords":    "polpette al sugo ricetta della nonna originale, polpette al sugo, ricetta polpette, polpette italiane ricetta originale, polpette di carne al sugo",
    "cal_num":     "420", "protein": "30g", "fat": "24g", "carbs": "18g",
    "ingredients": [
      "400g macinato di manzo (non troppo magro, 15-20% grasso)",
      "200g macinato di maiale (o salsiccia fresca spellata)",
      "80g mollica di pane raffermo (senza crosta)",
      "80ml latte intero",
      "2 uova grandi",
      "50g Parmigiano Reggiano grattugiato",
      "2 spicchi d'aglio, tritati finissimi",
      "Un mazzetto di prezzemolo fresco, tritato",
      "Sale, pepe nero macinato fresco, noce moscata q.b.",
      "700ml passata di pomodoro San Marzano",
      "2 spicchi d'aglio (per il sugo)",
      "4 foglie di basilico fresco",
      "3 cucchiai olio extravergine d'oliva",
      "Olio di semi di arachide per friggere",
    ],
    "steps": [
      "Ammolla la mollica di pane nel latte per 10 minuti. Poi strizzala bene con le mani fino a eliminare quasi tutto il latte — il pane deve essere umido ma non bagnato. Questo pane ammollato è il segreto della morbidezza.",
      "In una ciotola capiente, metti i macinati, il pane strizzato sbriciolato, le uova, il Parmigiano, l'aglio, il prezzemolo tritato, sale, pepe e noce moscata. Mescola con le mani per 2-3 minuti finché tutto è uniformemente amalgamato. Non lavorare troppo il composto.",
      "Con le mani leggermente umide, forma polpette della dimensione di una pallina da golf (circa 40-45g). Devono essere compatte ma non schiacciate. Con queste dosi otterrai circa 16-18 polpette.",
      "Scalda abbondante olio di semi in una padella capiente a fuoco medio-alto. Friggi le polpette in due batch per 3-4 minuti per lato, finché sono dorate su tutti i lati. Non devono essere cotte dentro. Scola su carta assorbente.",
      "Nella stessa padella, svuotata dall'olio di frittura, versa l'olio EVO e fai soffriggere l'aglio per 1 minuto. Aggiungi la passata di pomodoro, sale, pepe, un pizzico di zucchero e il basilico. Cuoci a fuoco medio per 5 minuti.",
      "Adagia le polpette rosolate nel sugo. Copri con un coperchio e cuoci a fuoco basso per 25-30 minuti, girandole delicatamente a metà cottura. Le polpette assorbono il sugo e diventano tenerissime.",
      "Servi con abbondante sugo, prezzemolo fresco e Parmigiano grattugiato. Accompagna con pane casereccio per la scarpetta — è obbligatorio.",
    ],
    "tips": [
      "Usa carne mista (manzo + maiale): il grasso del maiale rende le polpette morbide. Solo manzo → polpette asciutte.",
      "Il pane ammollato nel latte (non pangrattato) è il segreto della consistenza tenera e umida.",
      "Non saltare la rosolatura: crea una crosta che trattiene i succhi durante la cottura nel sugo.",
      "Le polpette finite nel sugo sono sempre più morbide: l'umidità le mantiene succose dall'interno.",
    ],
    "prose1_h2":  "Perché le Polpette della Nonna Sono Sempre Migliori: I 3 Segreti",
    "prose1":     """Il segreto delle polpette della nonna non è nella lista ingredienti — è nella tecnica. Le nonne usavano sempre il pane raffermo di due giorni ammollato nel latte, non il pangrattato industriale. Il pane assorbe i succhi della carne durante la cottura e li rilascia man mano che si mangia, creando una texture tenera e umida impossibile da ottenere con il pangrattato. Il secondo segreto è la carne: le nonne usavano carne mista — quello che avevano in casa — spesso con salsiccia che aggiunge sapore e grasso. Il terzo segreto è la cottura nel sugo: non in forno, non solo in padella — le polpette finiscono sempre nel sugo che le mantiene umide e le insaporisce dall'esterno.""",
    "prose2_h2":  "Polpette in Padella, al Forno o nel Sugo: Tutte le Differenze",
    "prose2":     """Le polpette cotte solo in padella sono croccanti fuori ma possono essere asciutte dentro. Le polpette al forno sono più leggere ma mancano del sapore della rosolatura. Le polpette cotte nel sugo (la tecnica tradizionale italiana) sono le più morbide: la carne finisce di cuocere nell'umidità del sugo, assorbendo il sapore del pomodoro, mentre il sugo a sua volta si arricchisce dei succhi della carne. Per le polpette perfette, la tecnica in tre fasi è insuperabile: forma → rosola → finisci nel sugo.""",
    "img2_alt":   "Polpette al sugo di pomodoro in piatto fondo bianco con basilico fresco e Parmigiano grattugiato sopra",
    "prose3_h2":  "Conservazione e Mille Usi delle Polpette Avanzate",
    "prose3":     """Le polpette al sugo si conservano in frigorifero per 3-4 giorni in un contenitore ermetico — migliorano il giorno dopo. Si congelano perfettamente con il loro sugo per 3 mesi. Le polpette avanzate sono versatili: schiacciale e usale come condimento per la pasta (il sugo diventa un ragù instant ottimo), mettile in un panino con mozzarella e basilico, o scaldale e servile su bruschetta di pane tostato. In Campania è tradizione usare le polpette al sugo per condire gli spaghetti come primo e servire le polpette come secondo — un solo sugo per due portate magnifiche.""",
    "faqs": [
      ("Posso usare solo manzo senza carne di maiale?", "Puoi, ma le polpette risulteranno più asciutte e meno saporite. Il grasso del maiale è quello che le rende morbide. Se vuoi usare solo manzo, scegli un macinato non troppo magro (almeno 15-20% di grasso) e aggiungi un cucchiaio di olio d'oliva nell'impasto per compensare la mancanza di grasso del maiale."),
      ("Perché le mie polpette si sgretolano durante la frittura?", "Le polpette si sfaldano quando l'impasto ha troppa umidità (pane non strizzato abbastanza), troppo poca colla (mancano le uova o il Parmigiano) o quando vengono girate troppo presto. Aspetta che si formi la crosticina prima di girarle — si staccano da sole dalla padella quando sono pronte."),
      ("Quanto grandi devono essere le polpette?", "La dimensione classica è quella di una pallina da golf, circa 40-45g. Polpette troppo grandi (oltre 60g) rischiano di rimanere crude dentro prima che si brucino fuori. Polpette troppo piccole si seccano rapidamente. La dimensione media garantisce cottura uniforme e la giusta proporzione crosta-interno morbido."),
      ("Si possono preparare le polpette il giorno prima?", "Assolutamente sì. Puoi preparare l'impasto la sera prima e conservarlo in frigorifero: il freddo compatta la carne e facilita la formatura. Puoi anche preparare le polpette complete con il sugo: il giorno dopo sono ancora più buone, con sapori più amalgamati."),
      ("Posso fare le polpette al forno invece che fritte?", "Sì per una versione più leggera: disponi le polpette su carta forno, irrora con un filo d'olio e inforna a 200°C per 20 minuti. Poi aggiungile al sugo per altri 15 minuti. Risparmierai olio ma il sapore della rosolatura sarà meno intenso. Per una versione ancora più leggera, metti le polpette crude direttamente nel sugo: ci vorranno 40-45 minuti a fuoco bassissimo."),
    ],
  },

  # ─── 25 — pasta alla gricia ───────────────────────────────
  {
    "slug":        "pasta-alla-gricia-ricetta",
    "title":       "Pasta alla Gricia Ricetta Originale Romana — La Madre della Carbonara e Amatriciana",
    "desc":        "La vera ricetta della pasta alla gricia: rigatoni, guanciale croccante e Pecorino Romano. La pasta romana più antica, madre della carbonara e dell'amatriciana. Ricetta originale in 20 minuti.",
    "tag":         "Pasta",
    "tag_color":   "#1565c0",
    "tag_bg":      "#e3f2fd",
    "h1":          "Pasta alla Gricia Ricetta Originale Romana — La Madre di Carbonara e Amatriciana",
    "intro":       "La gricia è la pasta romana più antica e meno conosciuta — eppure è la 'madre' di tutte le paste romane: dalla gricia nacque l'amatriciana (aggiungendo il pomodoro) e dalla gricia nacque la carbonara (aggiungendo l'uovo). Solo tre ingredienti: pasta, guanciale croccante e Pecorino Romano. Niente pomodoro, niente uova, niente panna. La gricia è pura essenza romana — povera negli ingredienti, infinitamente ricca nel sapore.",
    "prep":        "5 min", "cook": "15 min", "total": "20 min",
    "servings":    "2 porzioni", "calories": "~580", "difficulty": "Facile",
    "badge_text":  "20 Min",
    "cuisine":     "Italiana",
    "category":    "Pasta",
    "keywords":    "pasta alla gricia ricetta originale romana, pasta alla gricia, gricia ricetta, rigatoni alla gricia, pasta romana guanciale pecorino",
    "cal_num":     "580", "protein": "22g", "fat": "28g", "carbs": "62g",
    "ingredients": [
      "200g rigatoni (o tonnarelli, spaghetti grossi)",
      "150g guanciale (non pancetta, non bacon)",
      "80g Pecorino Romano DOP, grattugiato finemente",
      "Pepe nero in grani, da macinare fresco (molto abbondante)",
      "Sale solo per l'acqua della pasta",
    ],
    "steps": [
      "Taglia il guanciale a listarelle o cubetti di circa 1cm. Mettilo in una padella capiente fredda a fuoco medio-basso. Cuoci lentamente per 10-12 minuti finché il grasso è completamente sciolto e i pezzi sono dorati e croccanti. Non usare olio — il grasso del guanciale è sufficiente. Metti da parte il guanciale, lascia il grasso nella padella.",
      "Porta a ebollizione una pentola d'acqua leggermente salata (meno sale del solito: il Pecorino è molto sapido). Cuoci i rigatoni fino a 2 minuti prima del tempo indicato. Prima di scolare, conserva almeno 200ml di acqua di cottura amidacea.",
      "In una ciotola, mescola il Pecorino grattugiato con 2-3 cucchiai di acqua di cottura tiepida per formare una crema densa. Aggiungi pepe nero macinato fresco abbondante.",
      "Scola la pasta e trasferiscila nella padella con il grasso del guanciale a fuoco medio-basso. Aggiungi un mestolo di acqua di cottura e manteca la pasta per 1-2 minuti finché l'acqua è quasi assorbita.",
      "Togli la padella dal fuoco. Aggiungi la crema di Pecorino e mescola vigorosamente per 30-40 secondi, aggiungendo acqua di cottura un po' alla volta per ottenere una salsa lucida e cremosa. Lavora velocemente fuori dal fuoco.",
      "Rimetti il guanciale croccante nella pasta. Aggiungi un'ultima macinata generosa di pepe nero. Servi immediatamente con altro Pecorino a tavola.",
    ],
    "tips": [
      "Il guanciale deve partire da freddo in padella senza olio: il calore graduale scioglie il grasso uniformemente.",
      "Conserva molta acqua di cottura: è il collante tra pasta e Pecorino. Senza acqua amidacea il Pecorino si agglomera.",
      "Il Pecorino deve essere unito fuori dal fuoco: il calore eccessivo lo fa diventare filante invece che cremoso.",
      "Usa rigatoni: la forma rigata e il foro trattengono il grasso del guanciale e la crema di Pecorino meglio di tutto.",
    ],
    "prose1_h2":  "Gricia: La Pasta più Antica di Roma — Più Vecchia di Carbonara e Amatriciana",
    "prose1":     """La pasta alla gricia ha origini contadine e pastorali, probabilmente medievali. Il nome deriva secondo alcune teorie da 'Grisciano' — un piccolo paese nei Monti della Laga vicino ad Amatrice — dove i pastori portavano con sé i soli ingredienti che non si deterioravano durante i lunghi mesi di transumanza: guanciale stagionato, Pecorino Romano e pasta secca. Era il cibo di chi non aveva null'altro. Quando nel XVII-XVIII secolo arrivò il pomodoro dall'America, i romani aggiunsero il pomodoro alla gricia e nacque l'amatriciana. Nel XX secolo aggiunsero l'uovo e nacque la carbonara. La gricia è la matrice di tutta la cucina romana.""",
    "prose2_h2":  "Guanciale vs Pancetta vs Bacon: Perché Non È la Stessa Cosa",
    "prose2":     """Nella gricia il guanciale non è sostituibile. La pancetta ha un profilo aromatico diverso (più affumicata, meno sapida) e un diverso contenuto di grasso. Il bacon americano — completamente affumicato — cambia totalmente il carattere del piatto. Il guanciale (guancia di maiale stagionata con pepe e erbe) ha un grasso più morbido e aromatico che si scioglie diversamente in padella, creando quel fondo untuoso e profumato che è l'anima della gricia. Se non trovi il guanciale, usa la pancetta tesa non affumicata come ultimo sostituto — ma la gricia autentica è solo con il guanciale.""",
    "img2_alt":   "Pasta alla gricia con rigatoni al dente, guanciale croccante dorato e crema avvolgente di Pecorino Romano nella padella",
    "prose3_h2":  "Le Quattro Paste Romane: Gricia, Amatriciana, Carbonara e Cacio e Pepe",
    "prose3":     """Roma ha quattro paste identitarie, tutte basate sugli stessi ingredienti con varianti minime: la Gricia (guanciale + Pecorino), l'Amatriciana (guanciale + Pecorino + pomodoro), la Carbonara (guanciale + Pecorino + uovo) e la Cacio e Pepe (Pecorino + pepe, senza guanciale). Padroneggiarle tutte e quattro significa comprendere la logica della cucina romana povera: pochi ingredienti, tecnica precisa, risultati straordinari. La gricia è quella meno conosciuta fuori da Roma — ma è quella che i romani veri cucinano di più in casa, perché è la più veloce, la più semplice e la più saporita.""",
    "faqs": [
      ("La gricia è diversa dalla carbonara?", "Sì — la gricia è senza uova. La carbonara ha aggiunto l'uovo alla gricia nel XX secolo. La gricia è più antica, più semplice, e per molti romani è la preferita proprio per questa semplicità: solo pasta, guanciale e Pecorino. Non c'è rischio che le uova si rapprendano — la gricia perdona più errori pur richiedendo la stessa attenzione alla tecnica."),
      ("Che pasta usare per la gricia?", "I rigatoni sono la scelta classica — la forma rigata e il foro trattengono il grasso e la crema di Pecorino. I tonnarelli (spaghetti alla chitarra romani) sono la seconda scelta tradizionale. Evita formati lisci e sottili: l'impasto grasso e cremoso richiede una pasta che lo trattenga fisicamente."),
      ("Posso usare Parmigiano invece del Pecorino?", "No — o almeno, non per la gricia autentica. Il Pecorino Romano ha un sapore pungente e sapido che è l'anima del piatto. Il Parmigiano è più delicato e la gricia perde il suo carattere. Se il Pecorino è troppo forte per il tuo palato, usa un mix 50/50 Pecorino + Parmigiano come compromesso."),
      ("Come evito che il Pecorino si agglomeri?", "Il Pecorino si agglomera quando viene a contatto con il calore diretto. Mescola sempre fuori dal fuoco con abbondante acqua di cottura. L'acqua amidacea abbassa la temperatura e aiuta il Pecorino a emulsionarsi. Se si agglomera, aggiungi un mestolo di acqua bollente e mescola energicamente — di solito si recupera."),
      ("La gricia si può preparare in anticipo?", "No — come tutte le paste romane va mangiata immediatamente. Il guanciale croccante diventa molliccio e la crema di Pecorino si rappigli. Se avanza, riscaldala in padella con un po' di acqua a fuoco basso. Meglio calcolare le dosi esatte e non cucinarne troppa."),
    ],
  },

  # ─── 26 — parmigiana di melanzane ────────────────────────
  {
    "slug":        "parmigiana-di-melanzane-ricetta",
    "title":       "Parmigiana di Melanzane Ricetta Originale Napoletana — Il Capolavoro dell'Estate Italiana",
    "desc":        "La vera parmigiana di melanzane napoletana: melanzane fritte, sugo di pomodoro San Marzano, mozzarella e Parmigiano. La ricetta originale della nonna campana passo per passo.",
    "tag":         "Secondi",
    "tag_color":   "#c62828",
    "tag_bg":      "#ffebee",
    "h1":          "Parmigiana di Melanzane Ricetta Originale Napoletana — Il Capolavoro dell'Estate",
    "intro":       "La parmigiana di melanzane è uno dei piatti più amati della cucina italiana nel mondo. La versione napoletana — quella originale e più autentica — usa melanzane fritte nell'olio (non grigliate, non al forno), sugo di pomodoro San Marzano, fior di latte o mozzarella di bufala, e Parmigiano Reggiano. Il segreto non è nella ricetta ma in due operazioni spesso saltate: la salatura delle melanzane per eliminare l'acqua in eccesso, e la frittura in abbondante olio. La parmigiana è un piatto d'estate, di pazienza e di amore.",
    "prep":        "40 min", "cook": "45 min", "total": "1h 25min",
    "servings":    "6 porzioni", "calories": "~380", "difficulty": "Medio",
    "badge_text":  "Napoletana",
    "cuisine":     "Italiana",
    "category":    "Secondi",
    "keywords":    "parmigiana di melanzane ricetta originale napoletana, parmigiana di melanzane ricetta, parmigiana melanzane, melanzane alla parmigiana ricetta originale, come fare la parmigiana",
    "cal_num":     "380", "protein": "16g", "fat": "24g", "carbs": "26g",
    "ingredients": [
      "1.5kg melanzane (tipo violetta lunga napoletana, o rotonde)",
      "Sale grosso per la salatura",
      "Olio di semi di arachide per friggere (abbondante)",
      "700ml passata di pomodoro San Marzano (o pelati frullati)",
      "2 spicchi d'aglio + 2 spicchi d'aglio (per il sugo)",
      "6 foglie di basilico fresco",
      "3 cucchiai olio extravergine d'oliva",
      "400g fior di latte (o mozzarella di bufala ben sgocciolata)",
      "100g Parmigiano Reggiano DOP grattugiato",
      "3 uova sode a fette (opzionale, tradizione napoletana)",
      "Basilico fresco, sale, pepe, un pizzico di zucchero",
    ],
    "steps": [
      "Taglia le melanzane a fette di circa 7-8mm. Disponi su un colapasta a strati cospargendo ogni strato con sale grosso. Metti un peso sopra e lascia riposare per almeno 1 ora. Le melanzane rilasceranno acqua amarognola scura. Risciacqua bene e asciuga accuratamente con carta cucina — più asciutte sono, meglio friggono.",
      "Prepara il sugo: fai soffriggere l'aglio nell'olio EVO per 1 minuto. Aggiungi la passata di pomodoro, sale, pepe, zucchero e basilico. Cuoci 20 minuti a fuoco medio finché il sugo è addensato e saporito.",
      "Friggi le melanzane: scalda abbondante olio di semi (almeno 3cm di altezza) in una padella a 180°C. Friggi le fette poche alla volta per 2-3 minuti per lato, finché sono dorate e morbide. Non sovraffollare la padella. Scola su carta assorbente e tampona bene.",
      "Taglia il fior di latte a fette. Se è molto acquoso, lascialo su carta cucina per 30 minuti per perdere l'eccesso di siero.",
      "Preriscalda il forno a 180°C. In una teglia da forno, stendi un velo di sugo sul fondo. Poi strati di: melanzane fritte, sugo, mozzarella, uova sode (se le usi), Parmigiano, basilico. Ripeti per almeno 3-4 strati. Sull'ultimo strato: sugo abbondante, Parmigiano generoso e foglie di basilico.",
      "Copri con stagnola e inforna per 25 minuti. Rimuovi la stagnola e cuoci altri 15-20 minuti finché la superficie è dorata e il formaggio è fuso e leggermente gratinato.",
      "Lascia riposare almeno 20-30 minuti prima di servire — fondamentale: da calda è liquida, da tiepida si taglia e si serve perfettamente.",
    ],
    "tips": [
      "Non saltare la salatura: senza salatura le melanzane trattengono acqua e la parmigiana diventa un lago.",
      "Friggi nell'olio — non grigliare: le melanzane grigliate perdono cremosità e sapore.",
      "Lascia raffreddare 20-30 minuti prima di servire: da calda è liquida, tiepida o fredda è perfetta.",
      "Il fior di latte troppo acquoso rovina tutto: asciugalo sempre su carta prima di usarlo.",
    ],
    "prose1_h2":  "Parmigiana di Melanzane: Napoletana, Siciliana o di Parma? La Vera Origine del Nome",
    "prose1":     """Nonostante il nome, la parmigiana di melanzane non viene da Parma. Le origini sono contese tra Napoli e la Sicilia. La parola 'parmigiana' potrebbe derivare dal dialetto siciliano 'parmiciana' (le liste di legno delle persiane) per la disposizione a strati delle melanzane. Il Parmigiano nel nome è arrivato dopo, come ingrediente aggiunto nei secoli. La versione napoletana è considerata la più autentica: con melanzane fritte, sugo di San Marzano, fior di latte e — nella versione più tradizionale — le uova sode a fette come ingrediente aggiuntivo che aggiunge consistenza agli strati.""",
    "prose2_h2":  "Fior di Latte o Mozzarella di Bufala? Fritta o al Forno? Tutte le Varianti",
    "prose2":     """La versione napoletana tradizionale usa il fior di latte perché fonde meglio e non rilascia troppa acqua. La mozzarella di bufala è più saporita ma molto acquosa — va sgocciolata per ore. In Sicilia si usa spesso il caciocavallo stagionato. La parmigiana 'fritta' (senza forno, strati assemblati ancora caldi e serviti a temperatura ambiente) è un'altra variante napoletana popolare. La versione al forno è più diffusa perché più pratica. La scelta dipende dal tempo, dalla tradizione familiare e dal gusto personale — tutte le versioni sono autentiche.""",
    "img2_alt":   "Parmigiana di melanzane napoletana tagliata in porzione nel piatto bianco mostrando gli strati di melanzane fritte e mozzarella fusa",
    "prose3_h2":  "Conservazione, il Giorno Dopo e Mille Usi della Parmigiana Avanzata",
    "prose3":     """La parmigiana di melanzane si conserva in frigorifero per 3-4 giorni. Il sapore migliora notevolmente il giorno dopo: i sapori si amalgamano, gli strati si compattano e si taglia perfettamente. Si serve fredda, a temperatura ambiente o riscaldata in forno a 160°C per 15 minuti. Non congela bene: le melanzane diventano mollicce. La parmigiana avanzata è ottima come ripieno per una piadina, come condimento per la pasta (schiacci gli strati con una forchetta e ottieni un condimento straordinario), o come farcitura per calzoni e pizze al forno.""",
    "faqs": [
      ("Devo salare le melanzane?", "Sì — è un passaggio essenziale. La salatura elimina l'acqua in eccesso (che renderebbe la parmigiana liquida) e l'amaro naturale. Le melanzane moderne hanno meno amaro delle varietà antiche, ma la salatura serve ancora per eliminare l'acqua. Senza salatura la parmigiana finisce in un lago di liquido durante la cottura in forno."),
      ("Posso fare la parmigiana con le melanzane grigliate invece di fritte?", "Sì per una versione più leggera. Le melanzane grigliate assorbono meno olio e la parmigiana risulta meno ricca. Ma la versione tradizionale napoletana è con le melanzane fritte: la frittura crea una barriera che impedisce alle melanzane di cedere liquidi in forno. Il sapore è nettamente diverso e superiore."),
      ("Le uova sode sono necessarie?", "Nella versione napoletana originale sì — le uova sode a fette sono un ingrediente tradizionale della parmigiana campana. Non compaiono nella versione siciliana o nelle versioni del Nord Italia. Se non ti piacciono, omettile: la parmigiana resta ottima senza."),
      ("Perché la mia parmigiana è acquosa?", "Le cause principali sono: melanzane non salate o non asciugate, mozzarella troppo acquosa non sgocciolata, sugo troppo liquido, o tempo in forno insufficiente. Soluzione: sala sempre le melanzane, asciuga la mozzarella su carta per 30 minuti, usa un sugo denso, e lascia riposare la parmigiana 20-30 minuti dopo il forno prima di tagliarla."),
      ("La parmigiana di melanzane è vegetariana?", "Sì — nella versione senza uova sode è completamente vegetariana (non vegana per mozzarella e Parmigiano). Con le uova sode è ovo-vegetariana. Per una versione vegana: usa mozzarella di soia e lievito alimentare in scaglie al posto del Parmigiano — il risultato è sorprendentemente buono."),
    ],
  },

]


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="it">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="canonical" href="{domain}/{slug}/" />

  <!-- Open Graph / Pinterest -->
  <meta property="og:type" content="article" />
  <meta property="og:site_name" content="{site}" />
  <meta property="og:title" content="{h1}" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="{domain}/{slug}/image-1.jpg" />
  <meta property="og:image:width" content="1000" />
  <meta property="og:image:height" content="1333" />
  <meta property="og:url" content="{domain}/{slug}/" />
  <meta name="twitter:card" content="summary_large_image" />

  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@graph": [
      {{
        "@type": "Recipe",
        "name": "{h1}",
        "description": "{desc}",
        "image": ["{domain}/{slug}/image-1.jpg", "{domain}/{slug}/image-2.jpg"],
        "author": {{"@type": "Organization", "name": "{site}"}},
        "datePublished": "{date}",
        "prepTime": "PT{prep_iso}",
        "cookTime": "PT{cook_iso}",
        "totalTime": "PT{total_iso}",
        "recipeCategory": "{category}",
        "recipeCuisine": "{cuisine}",
        "keywords": "{keywords}",
        "recipeYield": "{servings}",
        "nutrition": {{
          "@type": "NutritionInformation",
          "calories": "{cal_num} calories",
          "proteinContent": "{protein}",
          "fatContent": "{fat}",
          "carbohydrateContent": "{carbs}"
        }},
        "recipeIngredient": {ingredients_json},
        "recipeInstructions": {steps_json},
        "aggregateRating": {{
          "@type": "AggregateRating",
          "ratingValue": "4.8",
          "ratingCount": "247",
          "bestRating": "5",
          "worstRating": "1"
        }}
      }},
      {{
        "@type": "FAQPage",
        "mainEntity": {faqs_json}
      }}
    ]
  }}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,400&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet" />

  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    :root {{
      --accent:      {tag_color};
      --accent-bg:   {tag_bg};
      --border:      #eeebe6;
      --text:        #1e1e1e;
      --muted:       #666;
    }}
    body {{
      font-family: 'Inter', sans-serif;
      background: #faf9f7;
      color: var(--text);
      line-height: 1.8;
      font-size: 17px;
    }}

    /* ── NAV ── */
    .topbar {{
      background: #1c1209;
      padding: 0 32px;
      height: 58px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      position: sticky;
      top: 0;
      z-index: 100;
    }}
    .topbar-logo {{
      font-family: 'Playfair Display', serif;
      font-size: 1.25rem;
      font-weight: 700;
      color: #fff;
      text-decoration: none;
      flex-shrink: 0;
      display: flex;
      align-items: center;
      gap: 9px;
    }}
    .topbar-logo em {{ color: #c9973a; font-style: italic; }}
    .topbar-nav {{
      display: flex;
      align-items: center;
      gap: 28px;
      list-style: none;
    }}
    .topbar-nav a {{
      font-size: 13px;
      font-weight: 500;
      color: rgba(255,255,255,0.7);
      text-decoration: none;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      transition: color 0.2s;
    }}
    .topbar-nav a:hover {{ color: #c9973a; }}

    /* ── LAYOUT ── */
    .page-wrap {{
      max-width: 820px;
      margin: 0 auto;
      padding: 40px 24px 80px;
    }}

    /* ── BREADCRUMB ── */
    .breadcrumb {{
      font-size: 13px;
      color: var(--muted);
      margin-bottom: 28px;
    }}
    .breadcrumb a {{ color: var(--accent); text-decoration: none; }}

    /* ── ARTICLE HEADER ── */
    .article-tag {{
      display: inline-block;
      background: var(--accent-bg);
      color: var(--accent);
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 1.8px;
      text-transform: uppercase;
      padding: 5px 14px;
      border-radius: 20px;
      margin-bottom: 18px;
    }}
    h1 {{
      font-family: 'Playfair Display', serif;
      font-size: clamp(1.9rem, 4vw, 2.7rem);
      line-height: 1.2;
      color: var(--text);
      margin-bottom: 18px;
    }}
    .article-intro {{
      font-size: 1.08rem;
      color: #4a4a4a;
      max-width: 700px;
      margin-bottom: 28px;
    }}

    /* ── FEATURED IMAGE ── */
    .featured-image-wrap {{ display: flex; justify-content: center; margin: 32px 0; }}
    .featured-image-inner {{
      position: relative;
      width: 100%;
      max-width: 440px;
      border-radius: 20px;
      overflow: hidden;
      box-shadow: 0 12px 40px rgba(0,0,0,0.14);
      transition: transform .35s, box-shadow .35s;
      cursor: pointer;
    }}
    .featured-image-inner:hover {{ transform: translateY(-6px) scale(1.02); box-shadow: 0 20px 56px rgba(0,0,0,.2); }}
    .featured-image-inner img {{ width: 100%; aspect-ratio: 3/4; object-fit: cover; display: block; }}
    .img-badge {{
      position: absolute; bottom: 14px; left: 14px;
      background: rgba(0,0,0,.55); backdrop-filter: blur(6px);
      color: #fff; font-size: 12px; font-weight: 600;
      padding: 5px 12px; border-radius: 20px; letter-spacing: .5px;
    }}

    /* ── PINTEREST ── */
    .pin-btn {{
      display: inline-flex; align-items: center; gap: 8px;
      background: #E60023; color: #fff;
      font-size: 14px; font-weight: 700;
      padding: 11px 22px; border-radius: 25px;
      text-decoration: none; margin-bottom: 36px;
      transition: opacity .2s;
    }}
    .pin-btn:hover {{ opacity: .88; }}

    /* ── META BADGES ── */
    .meta-row {{ display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 40px; }}
    .meta-badge {{
      background: #fff; border: 1.5px solid var(--border);
      border-radius: 12px; padding: 9px 18px;
      text-align: center; min-width: 80px;
    }}
    .meta-badge .lbl {{ display: block; font-size: 10px; color: #999; text-transform: uppercase; letter-spacing: 1px; }}
    .meta-badge .val {{ display: block; font-size: 15px; font-weight: 700; color: var(--text); margin-top: 2px; }}

    /* ── PROSE ── */
    .prose h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 1.55rem; color: var(--text);
      margin: 40px 0 14px; padding-bottom: 8px;
      border-bottom: 2px solid var(--border);
    }}
    .prose p {{ margin-bottom: 18px; }}
    .prose strong {{ color: var(--text); font-weight: 600; }}
    .prose em {{ font-style: italic; }}

    /* ── RECIPE CARD ── */
    .recipe-card {{
      background: #fff; border: 2px solid var(--accent);
      border-radius: 20px; padding: 36px;
      margin: 40px 0; box-shadow: 0 4px 20px rgba(0,0,0,.06);
    }}
    .card-title {{
      font-family: 'Playfair Display', serif;
      font-size: 1.35rem; font-weight: 700;
      color: var(--text); margin-bottom: 24px;
      padding-bottom: 16px; border-bottom: 2px solid var(--border);
    }}
    .ingredients-list {{ list-style: none; margin-bottom: 28px; }}
    .ingredients-list li {{
      padding: 10px 0; border-bottom: 1px solid var(--border);
      font-size: 15px;
    }}
    .ingredients-list li::before {{ content: "▸ "; color: var(--accent); font-size: 12px; }}
    .steps-list {{ padding-left: 20px; }}
    .steps-list li {{
      padding: 10px 0 10px 8px;
      border-bottom: 1px solid var(--border);
      font-size: 15px; line-height: 1.7;
    }}
    .steps-list li::marker {{ color: var(--accent); font-weight: 700; }}

    /* ── TIP BOX ── */
    .tip-box {{
      background: var(--accent-bg);
      border-left: 4px solid var(--accent);
      border-radius: 0 12px 12px 0;
      padding: 20px 24px; margin: 32px 0;
      font-size: 15px;
    }}
    .tip-box strong {{ display: block; margin-bottom: 12px; font-size: 16px; color: var(--accent); }}
    .tip-box ul {{ padding-left: 18px; }}
    .tip-box li {{ margin-bottom: 8px; }}

    /* ── MID IMAGE ── */
    .mid-image-wrap {{ display: flex; justify-content: center; margin: 36px 0; }}
    .mid-image-inner {{ border-radius: 16px; overflow: hidden; max-width: 400px; width: 100%; box-shadow: 0 8px 30px rgba(0,0,0,.12); }}
    .mid-image-inner img {{ width: 100%; display: block; }}

    /* ── FAQ ── */
    .faq-section {{ margin-top: 48px; }}
    .faq-section h2 {{
      font-family: 'Playfair Display', serif;
      font-size: 1.6rem; margin-bottom: 24px;
      padding-bottom: 12px; border-bottom: 2px solid var(--border);
    }}
    .faq-item {{ margin-bottom: 28px; }}
    .faq-item h3 {{ font-size: 1.05rem; font-weight: 600; color: var(--text); margin-bottom: 8px; }}
    .faq-item p {{ font-size: 15px; color: #444; }}

    /* ── FOOTER ── */
    footer {{
      background: #1c1209; color: rgba(255,255,255,.45);
      text-align: center; padding: 40px 24px;
      font-size: 13px; margin-top: 60px;
    }}
    footer a {{ color: rgba(255,255,255,.45); text-decoration: none; }}
    footer a:hover {{ color: #c9973a; }}

    @media(max-width:600px) {{
      .page-wrap {{ padding: 24px 16px 60px; }}
      .topbar {{ padding: 0 16px; }}
      .topbar-nav {{ gap: 16px; }}
      .topbar-nav a {{ font-size: 11px; }}
      .recipe-card {{ padding: 24px 20px; }}
      .meta-badge {{ padding: 8px 12px; min-width: 70px; }}
    }}
  </style>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':
  new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  }})(window,document,'script','dataLayer','GTM-5Q7MLKKM');</script>
  <!-- End Google Tag Manager -->
  <!-- Google AdSense -->
  <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4318681272939684" crossorigin="anonymous"></script>
  <!-- HB Agency Prebid -->
  <script src="https://d3u598arehftfk.cloudfront.net/prebid_hb_38809_40467.js" async></script>
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5Q7MLKKM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<nav class="topbar">
  <a href="/" class="topbar-logo"><svg width="14" height="18" viewBox="0 0 14 18" fill="none" aria-hidden="true"><path d="M7 17V7" stroke="#c9973a" stroke-width="1.5" stroke-linecap="round"/><path d="M7 7C7 4.5 4 2 1 2c0 3 2.5 5.5 6 5.5z" fill="#c9973a"/><path d="M7 11C7 8.5 10 6 13 6c0 3-2.5 5.5-6 5.5z" fill="#c9973a" opacity="0.75"/></svg><span><em>ital</em>ricette</span></a>
  <ul class="topbar-nav">
    <li><a href="../pasta/">Pasta</a></li>
    <li><a href="../antipasti/">Antipasti</a></li>
    <li><a href="../dolci/">Dolci</a></li>
    <li><a href="../secondi/">Secondi</a></li>
  </ul>
</nav>

<div class="page-wrap">

  <div class="breadcrumb">
    <a href="/">Home</a> &rsaquo; <a href="/#{category_anchor}">{tag}</a> &rsaquo; {h1}
  </div>

  <span class="article-tag">{tag}</span>
  <h1>{h1}</h1>
  <p class="article-intro">{intro}</p>

  <!-- Main Image -->
  <div class="featured-image-wrap">
    <div class="featured-image-inner">
      <img src="image-1.jpg"
           alt="{img1_alt}"
           width="440" height="587"
           loading="eager" />
      <span class="img-badge">{badge_text}</span>
    </div>
  </div>

  <!-- Pinterest -->
  <a class="pin-btn" href="https://pinterest.com/pin/create/button/?url={domain}/{slug}/&media={domain}/{slug}/image-1.jpg&description={h1}" target="_blank" rel="noopener">
    <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.373 0 0 5.373 0 12c0 5.084 3.163 9.426 7.627 11.174-.105-.949-.2-2.405.042-3.441.218-.937 1.407-5.965 1.407-5.965s-.359-.719-.359-1.782c0-1.668.967-2.914 2.171-2.914 1.023 0 1.518.769 1.518 1.69 0 1.029-.655 2.568-.994 3.995-.283 1.194.599 2.169 1.777 2.169 2.133 0 3.772-2.249 3.772-5.495 0-2.873-2.064-4.882-5.012-4.882-3.414 0-5.418 2.561-5.418 5.207 0 1.031.397 2.138.893 2.738a.36.36 0 0 1 .083.345l-.333 1.36c-.053.22-.174.267-.402.161-1.499-.698-2.436-2.889-2.436-4.649 0-3.785 2.75-7.262 7.929-7.262 4.163 0 7.398 2.967 7.398 6.931 0 4.136-2.607 7.464-6.227 7.464-1.216 0-2.359-.632-2.75-1.378l-.748 2.853c-.271 1.043-1.002 2.35-1.492 3.146C9.57 23.812 10.763 24 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0z"/></svg>
    Salva su Pinterest
  </a>

  <!-- Meta Badges -->
  <div class="meta-row">
    <div class="meta-badge"><span class="lbl">Preparazione</span><span class="val">{prep}</span></div>
    <div class="meta-badge"><span class="lbl">Cottura</span><span class="val">{cook}</span></div>
    <div class="meta-badge"><span class="lbl">Totale</span><span class="val">{total}</span></div>
    <div class="meta-badge"><span class="lbl">Porzioni</span><span class="val">{servings}</span></div>
    <div class="meta-badge"><span class="lbl">Calorie</span><span class="val">{calories}</span></div>
    <div class="meta-badge"><span class="lbl">Difficolt&agrave;</span><span class="val">{difficulty}</span></div>
  </div>

  <!-- Prose 1 -->
  <div class="prose">
    <h2>{prose1_h2}</h2>
    <p>{prose1}</p>
    <h2>{prose2_h2}</h2>
    <p>{prose2}</p>
  </div>

  <!-- Recipe Card -->
  <div class="recipe-card">
    <div class="card-title">{h1} — Ricetta Completa</div>
    <p style="font-size:1.1rem;font-weight:700;margin-bottom:16px;">Ingredienti</p>
    <ul class="ingredients-list">
{ingredients_html}
    </ul>
    <p style="font-size:1.1rem;font-weight:700;margin-bottom:16px;">Procedimento</p>
    <ol class="steps-list">
{steps_html}
    </ol>
  </div>

  <div class="tip-box">
    <strong>Consigli dello Chef</strong>
    <ul>
{tips_html}
    </ul>
  </div>

  <!-- Second Image -->
  <div class="mid-image-wrap">
    <div class="mid-image-inner">
      <img src="image-2.jpg" alt="{img2_alt}" width="400" height="533" loading="lazy" />
    </div>
  </div>

  <!-- Prose 3 -->
  <div class="prose">
    <h2>{prose3_h2}</h2>
    <p>{prose3}</p>
  </div>

  <!-- FAQ -->
  <section class="faq-section">
    <h2>Domande Frequenti</h2>
{faqs_html}
  </section>

</div>

<footer>
  &copy; 2026 <a href="/">italricette</a> &mdash; Tutti i diritti riservati &nbsp;|&nbsp;
  <a href="../privacy-policy.html">Privacy</a> &nbsp;|&nbsp;
  <a href="../disclaimer.html">Disclaimer</a>
</footer>

</body>
</html>
"""


import json
import re

def parse_time_to_iso(t: str) -> str:
    """'25 min' -> '25M', '1h 30min' -> '1H30M', '1h' -> '1H'"""
    t = re.sub(r'\(.*?\)', '', t).strip()
    hrs  = re.search(r'(\d+)\s*h(?:r|our)?s?\b', t, re.IGNORECASE)
    mins = re.search(r'(\d+)\s*min', t, re.IGNORECASE)
    result = ""
    if hrs:
        result += f"{hrs.group(1)}H"
    if mins:
        result += f"{mins.group(1)}M"
    return result or "0M"

def build(a: dict) -> str:
    ingredients_json = json.dumps(a["ingredients"], ensure_ascii=False)
    steps_json = json.dumps([
        {
            "@type": "HowToStep",
            "name": f"Passo {i+1}",
            "text": s,
            "url": f"{DOMAIN}/{a['slug']}/#step-{i+1}",
            "image": {
                "@type": "ImageObject",
                "url": f"{DOMAIN}/{a['slug']}/image-1.jpg"
            }
        }
        for i, s in enumerate(a["steps"])
    ], ensure_ascii=False)
    faqs_json = json.dumps([
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": ans}}
        for q, ans in a["faqs"]
    ], ensure_ascii=False)

    ingredients_html = "\n".join(f"      <li>{i}</li>" for i in a["ingredients"])
    steps_html       = "\n".join(f'      <li id="step-{i+1}">{s}</li>' for i, s in enumerate(a["steps"]))
    tips_html        = "\n".join(f"      <li>{t}</li>" for t in a["tips"])
    faqs_html        = "\n".join(
        f'    <div class="faq-item">\n'
        f'      <h3>{q}</h3>\n'
        f'      <p>{ans}</p>\n'
        f'    </div>'
        for q, ans in a["faqs"]
    )

    img1_alt = a["h1"]
    category_anchor = a["category"].lower().replace(" ", "-")

    return HTML_TEMPLATE.format(
        title=a["title"], desc=a["desc"], domain=DOMAIN, site=SITE, date=DATE,
        slug=a["slug"], h1=a["h1"], intro=a["intro"],
        tag=a["tag"], tag_color=a["tag_color"], tag_bg=a["tag_bg"],
        badge_text=a["badge_text"],
        prep=a["prep"], cook=a["cook"], total=a["total"],
        servings=a["servings"], calories=a["calories"], difficulty=a["difficulty"],
        prep_iso=parse_time_to_iso(a["prep"]),
        cook_iso=parse_time_to_iso(a["cook"]),
        total_iso=parse_time_to_iso(a["total"]),
        cuisine=a["cuisine"], category=a["category"], category_anchor=category_anchor,
        keywords=a["keywords"],
        cal_num=a["cal_num"], protein=a["protein"], fat=a["fat"], carbs=a["carbs"],
        ingredients_json=ingredients_json, steps_json=steps_json, faqs_json=faqs_json,
        ingredients_html=ingredients_html, steps_html=steps_html,
        tips_html=tips_html, faqs_html=faqs_html,
        img1_alt=img1_alt, img2_alt=a["img2_alt"],
        prose1_h2=a["prose1_h2"], prose1=a["prose1"].strip(),
        prose2_h2=a["prose2_h2"], prose2=a["prose2"].strip(),
        prose3_h2=a["prose3_h2"], prose3=a["prose3"].strip(),
    )


def main():
    print(f"Building {len(ARTICLES)} articles...")
    for a in ARTICLES:
        folder = BASE / a["slug"]
        folder.mkdir(exist_ok=True)
        html = build(a)
        (folder / "index.html").write_text(html, encoding="utf-8")
        print(f"  OK  {a['slug']}/index.html")
    print(f"\nDone! {len(ARTICLES)} articles generated.")

if __name__ == "__main__":
    main()
