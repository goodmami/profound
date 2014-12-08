profound
========

Pronoun Finder

Dependencies:

 * [PyDelphin](https://github.com/goodmami/pydelphin)

## Command-line Usage

If a SimpleMRS input has a surface string, the relevant substrings will
be highlighted to show the pronouns (below shown surrounded by asterisks):

    $ profound.sh < where-did-the-dog-bark.mrs 
    *Where* did the dog bark?

If the matched pronoun EP does not have a surface substring, empty braces
are highlighted where it should be:

    $ profound.sh < ~/pronouns/speak-now.mrs 
    Speak now.
    *{}*Speak now.
    *{}*Speak now.
    Speak now.

If no surface string is given in the SimpleMRS, the EP string is shown
instead:

    profound.sh < who-barked_no-surface.mrs
    which_q_rel *person_rel* "_bark_v_1_rel"
