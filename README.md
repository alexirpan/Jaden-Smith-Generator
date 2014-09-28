Jaden-Smith-Generator
=====================

Typical sentences with Markov Chain trained on Jaden Smith tweets + King James Bible

This uses a combined corpus of tweets by Jaden Smith (up to Sep 27, 2014), and the King James Bible.
This counts the frequency of a word appearing given the previous word, then samples from that distribution to create a "typical" sentence.
(Since the King James Bible is much longer, the word counts from it have much smaller weight.)
