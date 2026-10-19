/**
 * content_eow2.js — REAL EOW2 grammar content layer.
 *
 * Authored from the teacher-approved Pilot-Run generators
 * (08_Pilot_Runs/2026-06-16-eow2-u#-voc-gram/generator_color.py + eow2lib.py).
 * Each unit's items use ONLY that unit's grammar focus and vocabulary.
 *
 * Shape:
 *   CONTENT_EOW2["<unit>"].grammar["<patternId>"] = [ ...items matching render_grammar schemas... ]
 *
 * Pattern ids match index.html PATTERNS keys (lowercase):
 *   fillblank, circlecorrect, truefalse, mc, sentencebuilder,
 *   scrambledsentences, sentencecompletion.
 *
 * English only. pic slugs are verified real folders under ../09_Image_Library/words/.
 */
const CONTENT_EOW2 = {

  /* ───────────── U1 Animal Friends — "They are + verb-ing" + word order ───────────── */
  "1": {
    grammar: {
      fillblank: [
        { text: "The birds are ___.", answer: "flying", pic: "fly" },
        { text: "The ducks are ___.", answer: "swimming", pic: "swim" },
        { text: "The cats are ___.", answer: "climbing", pic: "climb" },
        { text: "The turtles are ___.", answer: "crawling", pic: "crawl" },
        { text: "The goats are ___ the hill.", answer: "climbing", pic: "goat" },
        { text: "The fish are ___ in the river.", answer: "swimming", pic: "swim" },
        { text: "The birds are ___ in the sky.", answer: "flying", pic: "fly" },
        { text: "The babies are ___ on the floor.", answer: "crawling", pic: "crawl" }
      ],
      circlecorrect: [
        { text: "The birds ___ flying.", options: ["are", "is"], answer: "are", pic: "fly" },
        { text: "The duck ___ swimming.", options: ["is", "are"], answer: "is", pic: "duck" },
        { text: "The cats ___ climbing.", options: ["are", "is"], answer: "are", pic: "cat" },
        { text: "The turtle ___ crawling.", options: ["is", "are"], answer: "is", pic: "turtle" },
        { text: "The goats ___ climbing.", options: ["are", "is"], answer: "are", pic: "goat" },
        { text: "The horse ___ swimming.", options: ["is", "are"], answer: "is", pic: "horse" },
        { text: "The birds ___ flying high.", options: ["are", "is"], answer: "are", pic: "fly" },
        { text: "The dog ___ swimming.", options: ["is", "are"], answer: "is", pic: "dog" }
      ],
      scrambledsentences: [
        { words: ["climbing", "the", "cats", "are"], answer: "The cats are climbing." },
        { words: ["the", "ducks", "are", "swimming"], answer: "The ducks are swimming." },
        { words: ["crawling", "the", "turtles", "are"], answer: "The turtles are crawling." },
        { words: ["flying", "the", "birds", "are"], answer: "The birds are flying." },
        { words: ["are", "the", "goats", "climbing"], answer: "The goats are climbing." },
        { words: ["the", "horse", "is", "swimming"], answer: "The horse is swimming." },
        { words: ["the", "cat", "is", "crawling"], answer: "The cat is crawling." },
        { words: ["are", "the", "fish", "swimming"], answer: "The fish are swimming." }
      ],
      sentencebuilder: [
        { words: ["are", "climbing", "The", "cats"], answer: "The cats are climbing." },
        { words: ["swimming", "are", "The", "ducks"], answer: "The ducks are swimming." },
        { words: ["The", "are", "turtles", "crawling"], answer: "The turtles are crawling." },
        { words: ["flying", "are", "The", "birds"], answer: "The birds are flying." },
        { words: ["climbing", "are", "The", "goats"], answer: "The goats are climbing." },
        { words: ["is", "The", "horse", "swimming"], answer: "The horse is swimming." },
        { words: ["crawling", "is", "The", "cat"], answer: "The cat is crawling." },
        { words: ["The", "dog", "is", "swimming"], answer: "The dog is swimming." }
      ]
    }
  },

  /* ───────────── U2 Fun in Class — "We're + verb-ing" ───────────── */
  "2": {
    grammar: {
      fillblank: [
        { text: "We're ___.", answer: "coloring", pic: "coloring" },
        { text: "We're ___.", answer: "counting", pic: "counting" },
        { text: "We're ___.", answer: "cutting", pic: "cutting" },
        { text: "We're ___.", answer: "drawing", pic: "drawing" },
        { text: "We're ___.", answer: "gluing", pic: "gluing" },
        { text: "We're ___ a picture.", answer: "drawing", pic: "drawing" },
        { text: "We're ___ the paper.", answer: "cutting", pic: "cutting" },
        { text: "We're ___ the stars.", answer: "counting", pic: "counting" },
        { text: "We're ___ to the teacher.", answer: "talking", pic: "talking" },
        { text: "We're ___ with crayons.", answer: "coloring", pic: "coloring" }
      ],
      circlecorrect: [
        { text: "We ___ counting crayons.", options: ["are", "is"], answer: "are", pic: "counting" },
        { text: "We ___ drawing a cat.", options: ["are", "is"], answer: "are", pic: "drawing" },
        { text: "We ___ cutting paper.", options: ["are", "is"], answer: "are", pic: "cutting" },
        { text: "We ___ coloring a picture.", options: ["are", "is"], answer: "are", pic: "coloring" },
        { text: "We ___ gluing the paper.", options: ["are", "is"], answer: "are", pic: "gluing" },
        { text: "We ___ talking in class.", options: ["are", "is"], answer: "are", pic: "talking" },
        { text: "We ___ counting markers.", options: ["are", "is"], answer: "are", pic: "marker" },
        { text: "We ___ using scissors.", options: ["are", "is"], answer: "are", pic: "scissors" }
      ],
      mc: [
        { text: "Are there any markers?", options: ["Yes, there are.", "No, there aren't.", "It is a marker."], answer: 0, pic: "marker" },
        { text: "Are there any crayons?", options: ["Yes, there are.", "No, there aren't.", "Yes, I am."], answer: 1 },
        { text: "Are there any notebooks?", options: ["Yes, there are.", "No, there aren't.", "It is a desk."], answer: 0, pic: "notebook" },
        { text: "Are there any scissors?", options: ["Yes, there are.", "No, there aren't.", "She is happy."], answer: 0, pic: "scissors" },
        { text: "Are there any paintbrushes?", options: ["Yes, there are.", "No, there aren't.", "It is glue."], answer: 0, pic: "paintbrush" },
        { text: "What are you doing?", options: ["We're cutting paper.", "Yes, there are.", "It is a marker."], answer: 0, pic: "cutting" },
        { text: "What are you doing?", options: ["We're drawing a cat.", "No, there aren't.", "She is tall."], answer: 0, pic: "drawing" },
        { text: "What are you doing?", options: ["We're counting crayons.", "Yes, it is.", "It is a desk."], answer: 0, pic: "counting" }
      ]
    }
  },

  /* ───────────── U3 Boots and Bathing Suits — "It's + weather" + imperatives ───────────── */
  "3": {
    grammar: {
      fillblank: [
        { text: "It's ___.", answer: "sunny", pic: "sunny" },
        { text: "It's ___.", answer: "rainy", pic: "rainy" },
        { text: "It's ___.", answer: "cloudy", pic: "cloudy" },
        { text: "It's ___.", answer: "hot", pic: "hot" },
        { text: "It's ___.", answer: "cold", pic: "cold" },
        { text: "It's ___ today. Put on your coat.", answer: "cold", pic: "cold" },
        { text: "It's ___. Take your umbrella.", answer: "rainy", pic: "rainy" },
        { text: "It's ___. Wear your bathing suit.", answer: "hot", pic: "hot" },
        { text: "It's ___. Wear your shorts.", answer: "sunny", pic: "sunny" },
        { text: "It's ___. The sky is grey.", answer: "cloudy", pic: "cloudy" }
      ],
      circlecorrect: [
        { text: "It's ___. Put on your coat.", options: ["cold", "hot"], answer: "cold", pic: "cold" },
        { text: "It's ___. Take your umbrella.", options: ["rainy", "sunny"], answer: "rainy", pic: "rainy" },
        { text: "It's ___. Wear your shorts.", options: ["hot", "cold"], answer: "hot", pic: "hot" },
        { text: "It's ___. The sun is out.", options: ["sunny", "rainy"], answer: "sunny", pic: "sunny" },
        { text: "It's ___. The sky is grey.", options: ["cloudy", "sunny"], answer: "cloudy", pic: "cloudy" },
        { text: "It's cold. Put on your ___.", options: ["coat", "shorts"], answer: "coat", pic: "coat" },
        { text: "It's rainy. Wear your ___.", options: ["raincoat", "sneakers"], answer: "raincoat", pic: "raincoat" },
        { text: "It's hot. Wear your ___.", options: ["bathing suit", "boots"], answer: "bathing suit", pic: "bathing-suit" }
      ],
      mc: [
        { text: "It's cold.", options: ["Put on your coat.", "Put on your shorts."], answer: 0, pic: "cold" },
        { text: "It's rainy.", options: ["Forget your umbrella.", "Take your umbrella."], answer: 1, pic: "rainy" },
        { text: "It's hot.", options: ["Put on your bathing suit.", "Put on your boots."], answer: 0, pic: "hot" },
        { text: "It's sunny.", options: ["Wear your raincoat.", "Wear your shorts."], answer: 1, pic: "sunny" },
        { text: "It's cold.", options: ["Wear your boots.", "Wear your bathing suit."], answer: 0, pic: "cold" },
        { text: "It's rainy.", options: ["Wear your raincoat.", "Wear your shorts."], answer: 0, pic: "rainy" },
        { text: "It's hot.", options: ["Wear your shorts.", "Wear your coat."], answer: 0, pic: "hot" },
        { text: "It's sunny.", options: ["Take your umbrella.", "Wear your sneakers."], answer: 1, pic: "sunny" }
      ]
    }
  },

  /* ───────────── U4 Fun in the Sun — "Do you like to...?" + "Let's..." ───────────── */
  "4": {
    grammar: {
      scrambledsentences: [
        { words: ["a", "ball", "Let's", "throw"], answer: "Let's throw a ball." },
        { words: ["catch", "Let's", "a", "ball"], answer: "Let's catch a ball." },
        { words: ["play", "Let's", "tag"], answer: "Let's play tag." },
        { words: ["a", "Let's", "ball", "bounce"], answer: "Let's bounce a ball." },
        { words: ["a", "game", "Let's", "play"], answer: "Let's play a game." },
        { words: ["Let's", "play", "soccer"], answer: "Let's play soccer." },
        { words: ["a", "kite", "Let's", "fly"], answer: "Let's fly a kite." },
        { words: ["a", "bike", "Let's", "ride"], answer: "Let's ride a bike." }
      ],
      sentencebuilder: [
        { words: ["Let's", "throw", "a", "ball"], answer: "Let's throw a ball." },
        { words: ["a", "Let's", "ball", "catch"], answer: "Let's catch a ball." },
        { words: ["tag", "Let's", "play"], answer: "Let's play tag." },
        { words: ["bounce", "a", "Let's", "ball"], answer: "Let's bounce a ball." },
        { words: ["play", "a", "game", "Let's"], answer: "Let's play a game." },
        { words: ["soccer", "Let's", "play"], answer: "Let's play soccer." },
        { words: ["fly", "a", "Let's", "kite"], answer: "Let's fly a kite." },
        { words: ["ride", "a", "bike", "Let's"], answer: "Let's ride a bike." }
      ],
      mc: [
        { text: "Do you like to play baseball?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "play-baseball" },
        { text: "Do you like to ride a bike?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "ride-a-bike" },
        { text: "Do you like to jump rope?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "jump-rope" },
        { text: "Do you like to play soccer?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "play-soccer" },
        { text: "Do you like to fly a kite?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "fly-a-kite" },
        { text: "Do you like to play tag?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "play-tag" },
        { text: "Do you like to catch a ball?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "catch-a-ball" },
        { text: "Do you like to play a game?", options: ["Yes, I do.", "No, I don't."], answer: 0, pic: "play-a-game" }
      ],
      sentencecompletion: [
        { stem: "I like to", pic: "play-soccer" },
        { stem: "After school, I like to" },
        { stem: "On a sunny day, I like to" },
        { stem: "With my friends, I like to" },
        { stem: "In the park, I like to" },
        { stem: "Let's" },
        { stem: "I like to play" },
        { stem: "I don't like to" }
      ]
    }
  },

  /* ───────────── U5 Inside Our House — prepositions + it/they ───────────── */
  "5": {
    grammar: {
      fillblank: [
        { text: "The cat is ___ the table.", answer: "on" },
        { text: "The cat is ___ the table.", answer: "under" },
        { text: "The cat is ___ to the table.", answer: "next" },
        { text: "The cat is ___ the table.", answer: "behind" },
        { text: "The phone is ___ the living room.", answer: "in", pic: "phone" },
        { text: "The stove is ___ the kitchen.", answer: "in", pic: "stove" },
        { text: "The tub is ___ the bathroom.", answer: "in", pic: "tub" },
        { text: "The rug is ___ the floor.", answer: "on", pic: "rug" }
      ],
      circlecorrect: [
        { text: "Where is the phone? ___ in the living room.", options: ["It's", "They're"], answer: "It's", pic: "phone" },
        { text: "Where are the books? ___ in the bedroom.", options: ["They're", "It's"], answer: "They're", pic: "bookcase" },
        { text: "Where is the stove? ___ in the kitchen.", options: ["It's", "They're"], answer: "It's", pic: "stove" },
        { text: "Where is the tub? ___ in the bathroom.", options: ["It's", "They're"], answer: "It's", pic: "tub" },
        { text: "Where is the rug? ___ on the floor.", options: ["It's", "They're"], answer: "It's", pic: "rug" },
        { text: "Where are the stairs? ___ next to the door.", options: ["They're", "It's"], answer: "They're", pic: "stairs" },
        { text: "Where is the sink? ___ in the kitchen.", options: ["It's", "They're"], answer: "It's", pic: "sink" },
        { text: "Where is the window? ___ in the living room.", options: ["It's", "They're"], answer: "It's", pic: "window" }
      ],
      mc: [
        { text: "Where is the phone?", options: ["It's in the living room.", "They're in the kitchen."], answer: 0, pic: "phone" },
        { text: "Where is the stove?", options: ["It's in the kitchen.", "They're in the bedroom."], answer: 0, pic: "stove" },
        { text: "Where are the books?", options: ["They're in the bedroom.", "It's in the kitchen."], answer: 0, pic: "bookcase" },
        { text: "Where is the tub?", options: ["It's in the bathroom.", "They're on the floor."], answer: 0, pic: "tub" },
        { text: "Where is the rug?", options: ["It's on the floor.", "They're in the tub."], answer: 0, pic: "rug" },
        { text: "Where is the sink?", options: ["It's in the kitchen.", "They're in the living room."], answer: 0, pic: "sink" },
        { text: "Where is the window?", options: ["It's in the living room.", "They're in the tub."], answer: 0, pic: "window" },
        { text: "Where is the door?", options: ["It's next to the stairs.", "They're on the floor."], answer: 0, pic: "door" }
      ]
    }
  },

  /* ───────────── U6 Day by Day — telling time + always/never/every day ───────────── */
  "6": {
    grammar: {
      fillblank: [
        { text: "It's ___ . I get up.", answer: "7:00", pic: "get-up" },
        { text: "It's ___ . I eat lunch.", answer: "12:00", pic: "eat-lunch" },
        { text: "It's ___ . I play with friends.", answer: "3:00", pic: "play-with-friends" },
        { text: "It's ___ . I eat dinner.", answer: "6:00", pic: "eat-dinner" },
        { text: "It's ___ . I go to bed.", answer: "9:00", pic: "go-to-bed" },
        { text: "I ___ get up in the morning.", answer: "always", pic: "get-up" },
        { text: "I ___ go to school in the morning.", answer: "always", pic: "go-to-school" },
        { text: "I go to bed ___ night.", answer: "at", pic: "go-to-bed" }
      ],
      circlecorrect: [
        { text: "I ___ get up in the morning.", options: ["always", "never"], answer: "always", pic: "get-up" },
        { text: "I ___ eat dinner in the morning.", options: ["never", "always"], answer: "never", pic: "eat-dinner" },
        { text: "I ___ go to bed at night.", options: ["always", "never"], answer: "always", pic: "go-to-bed" },
        { text: "I ___ go to school at night.", options: ["never", "always"], answer: "never", pic: "go-to-school" },
        { text: "I brush my teeth ___ day.", options: ["every", "never"], answer: "every", pic: "brush-my-teeth" },
        { text: "I ___ eat breakfast in the morning.", options: ["always", "never"], answer: "always", pic: "eat-breakfast" },
        { text: "I ___ get up at night.", options: ["never", "always"], answer: "never", pic: "get-up" },
        { text: "I eat lunch ___ day.", options: ["every", "never"], answer: "every", pic: "eat-lunch" }
      ],
      mc: [
        { text: "I ___ get up in the morning.", options: ["always", "never"], answer: 0, pic: "get-up" },
        { text: "I ___ eat dinner in the morning.", options: ["always", "never"], answer: 1, pic: "eat-dinner" },
        { text: "I go to school ______ .", options: ["every day", "at night"], answer: 0, pic: "go-to-school" },
        { text: "I ___ go to bed at night.", options: ["always", "never"], answer: 0, pic: "go-to-bed" },
        { text: "I ___ brush my teeth in the morning.", options: ["always", "never"], answer: 0, pic: "brush-my-teeth" },
        { text: "I ___ eat breakfast at night.", options: ["always", "never"], answer: 1, pic: "eat-breakfast" },
        { text: "I get up ______ .", options: ["in the morning", "at night"], answer: 0, pic: "get-up" },
        { text: "I eat dinner ______ .", options: ["in the evening", "in the morning"], answer: 0, pic: "eat-dinner" }
      ]
    }
  },

  /* ───────────── U7 How Are You? — "looks + adjective" + plurals ───────────── */
  "7": {
    grammar: {
      mc: [
        { text: "He looks ___.", options: ["angry", "happy"], answer: 0, pic: "angry" },
        { text: "She looks ___.", options: ["tired", "hungry"], answer: 0, pic: "tired" },
        { text: "He looks ___.", options: ["scared", "bored"], answer: 0, pic: "scared" },
        { text: "She looks ___.", options: ["thirsty", "surprised"], answer: 1, pic: "surprised" },
        { text: "She looks ___.", options: ["bored", "angry"], answer: 0, pic: "bored" },
        { text: "He looks ___.", options: ["hungry", "tired"], answer: 0, pic: "hungry" },
        { text: "She looks ___.", options: ["thirsty", "scared"], answer: 0, pic: "thirsty" },
        { text: "He looks ___.", options: ["tired", "angry"], answer: 0, pic: "tired" }
      ],
      fillblank: [
        { text: "one book  ->  two ___", answer: "books" },
        { text: "one parent  ->  two ___", answer: "parents" },
        { text: "one child  ->  two ___", answer: "children" },
        { text: "one person  ->  three ___", answer: "people" },
        { text: "one foot  ->  two ___", answer: "feet" },
        { text: "one tooth  ->  two ___", answer: "teeth" },
        { text: "one boy  ->  two ___", answer: "boys" },
        { text: "one girl  ->  two ___", answer: "girls" }
      ],
      circlecorrect: [
        { text: "He ___ angry.", options: ["looks", "look"], answer: "looks", pic: "angry" },
        { text: "She ___ tired.", options: ["looks", "look"], answer: "looks", pic: "tired" },
        { text: "He ___ scared.", options: ["looks", "look"], answer: "looks", pic: "scared" },
        { text: "She ___ surprised.", options: ["looks", "look"], answer: "looks", pic: "surprised" },
        { text: "one child  ->  two ___", options: ["children", "childs"], answer: "children" },
        { text: "one foot  ->  two ___", options: ["feet", "foots"], answer: "feet" },
        { text: "one person  ->  three ___", options: ["people", "persons"], answer: "people" },
        { text: "one book  ->  two ___", options: ["books", "bookes"], answer: "books" }
      ]
    }
  },

  /* ───────────── U8 Awesome Animals — can/can't + "Does ... have ...?" ───────────── */
  "8": {
    grammar: {
      truefalse: [
        { text: "A penguin can swim.", answer: true, pic: "penguin" },
        { text: "A penguin can fly.", answer: false, pic: "penguin" },
        { text: "A kangaroo can hop.", answer: true, pic: "kangaroo" },
        { text: "A tiger can fly.", answer: false, pic: "tiger" },
        { text: "A lion can run.", answer: true, pic: "lion" },
        { text: "A panda can climb.", answer: true, pic: "panda" },
        { text: "A zebra can swim.", answer: false, pic: "zebra" },
        { text: "A giraffe can hop.", answer: false, pic: "giraffe" }
      ],
      mc: [
        { text: "Does a tiger have sharp claws?", options: ["Yes, it does.", "No, it doesn't."], answer: 0, pic: "tiger" },
        { text: "Does a lion have big teeth?", options: ["Yes, it does.", "No, it doesn't."], answer: 0, pic: "lion" },
        { text: "Does a panda have a short tail?", options: ["Yes, it does.", "No, it doesn't."], answer: 0, pic: "panda" },
        { text: "Does a zebra have a long trunk?", options: ["Yes, it does.", "No, it doesn't."], answer: 1, pic: "zebra" },
        { text: "Does a giraffe have sharp claws?", options: ["Yes, it does.", "No, it doesn't."], answer: 1, pic: "giraffe" },
        { text: "Does a hippo have big teeth?", options: ["Yes, it does.", "No, it doesn't."], answer: 0, pic: "hippo" },
        { text: "Does a penguin have colorful feathers?", options: ["Yes, it does.", "No, it doesn't."], answer: 1, pic: "penguin" },
        { text: "Does a kangaroo have a long tail?", options: ["Yes, it does.", "No, it doesn't."], answer: 0, pic: "kangaroo" }
      ],
      circlecorrect: [
        { text: "A penguin ___ swim.", options: ["can", "can't"], answer: "can", pic: "penguin" },
        { text: "A penguin ___ fly.", options: ["can't", "can"], answer: "can't", pic: "penguin" },
        { text: "A kangaroo ___ hop.", options: ["can", "can't"], answer: "can", pic: "kangaroo" },
        { text: "A tiger ___ fly.", options: ["can't", "can"], answer: "can't", pic: "tiger" },
        { text: "A lion ___ run.", options: ["can", "can't"], answer: "can", pic: "lion" },
        { text: "A panda ___ climb.", options: ["can", "can't"], answer: "can", pic: "panda" },
        { text: "A giraffe ___ hop.", options: ["can't", "can"], answer: "can't", pic: "giraffe" },
        { text: "A zebra ___ run.", options: ["can", "can't"], answer: "can", pic: "zebra" }
      ]
    }
  }

};
