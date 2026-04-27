"""
Sapori d'Italia — Article Generator
Run: python build_articles.py
"""

from pathlib import Path

BASE   = Path(__file__).parent
DOMAIN = "https://saporidItalia.it"
SITE   = "Sapori d'Italia"
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
        "recipeYield": "{servings} servings",
        "nutrition": {{
          "@type": "NutritionInformation",
          "calories": "{cal_num} calories",
          "proteinContent": "{protein}",
          "fatContent": "{fat}",
          "carbohydrateContent": "{carbs}"
        }},
        "recipeIngredient": {ingredients_json},
        "recipeInstructions": {steps_json}
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
    }}
    .topbar-logo span {{ color: #c9973a; font-style: italic; }}
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
</head>
<body>
<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-5Q7MLKKM"
height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->

<nav class="topbar">
  <a href="/" class="topbar-logo">Sapori <span>d'Italia</span></a>
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
  &copy; 2026 <a href="/">Sapori d'Italia</a> &mdash; Tutti i diritti riservati &nbsp;|&nbsp;
  <a href="../privacy-policy.html">Privacy</a> &nbsp;|&nbsp;
  <a href="../disclaimer.html">Disclaimer</a>
</footer>

</body>
</html>
"""


import json
import re

def parse_time_to_iso(t: str) -> str:
    """'25 min' -> '25M', '1 hr 30 min' -> '1H30M', '4 hrs (chill)' -> '4H'"""
    t = re.sub(r'\(.*?\)', '', t).strip()
    hrs = re.search(r'(\d+)\s*hr', t)
    mins = re.search(r'(\d+)\s*min', t)
    result = ""
    if hrs:
        result += f"{hrs.group(1)}H"
    if mins:
        result += f"{mins.group(1)}M"
    return result or "0M"

def build(a: dict) -> str:
    ingredients_json = json.dumps(a["ingredients"], ensure_ascii=False)
    steps_json = json.dumps([
        {"@type": "HowToStep", "text": s} for s in a["steps"]
    ], ensure_ascii=False)
    faqs_json = json.dumps([
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": ans}}
        for q, ans in a["faqs"]
    ], ensure_ascii=False)

    ingredients_html = "\n".join(f"      <li>{i}</li>" for i in a["ingredients"])
    steps_html       = "\n".join(f"      <li>{s}</li>" for s in a["steps"])
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
