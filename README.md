<img src='https://raw.githubusercontent.com/takusui/Kat.ai/master/git/kat-logo.png' height="80">

Kat.ai is a multi-platform chatbot that adapts while talking with you. This project aims to speed up the development of intelligent bots and make them available for anyone who has enough computing power. Kat will be able to run in any environment and, by using an adaptable sequence to sequence model, speak any language.

There are many posibilities when it comes to the customization:
* Add your own 3D or 2D models and backgrounds.
* Add your own voice bank.
* Implement custom commands.
* Sculpt Kat's personality to match your taste.
* Add pictures of you or of your friends so she can recognize you/them.

## Brain structure
![](https://raw.githubusercontent.com/takusui/Kat.ai/master/git/brain.png)

This project will focus on mimicking the human brain using neural networks.

### Language comprehension
Kat.ai will use a minimally trained sequence-to-sequence model built in Tensorflow to answer your questions.

![](https://raw.githubusercontent.com/takusui/Kat.ai/0e74c223a9b6e5eae9f37110425379dd58e1f4e8/git/seq2seq.png)

The model will try to improve itself by asking questions about words that it hasn't encountered before or by searching their definition on the internet. If one is found, you will be asked to confirm if it is correct. Obviously, if you trust a source, you can make the bot learn without asking you. It will try to identify idioms on its own and add them to the database.

To start with, I will train it for the English language and slowly move on to Chinese, Spanish, French and other languages that have enough samples to feed the model. Things will get really interesting when I'll have to find a way to avoid learning only one definition for a word.



### Speech
I will use the deep generative model of raw audio waveforms made by DeepMind, [WaveNet](https://deepmind.com/blog/wavenet-generative-model-raw-audio/). Here is an [example](https://storage.googleapis.com/deepmind-media/pixie/us-english/wavenet-1.wav) of what it is capable of. 

### Hearing
For now, Mozzila's [DeepSpeech](https://github.com/mozilla/DeepSpeech) seems promising. 

### Image/object recognition
Tensorflow already has an [Object detection API](https://github.com/tensorflow/models/tree/master/research/object_detection) which works perfectly for the objective of this project.

### Text recognition
A real time implementation will most likely be done using the system above to save some computing power. A place to start researching more about this would be [EAST](https://github.com/argman/EAST).

### Facial recognition
The first step is to choose the most efficient system between [OpenFace](https://github.com/cmusatyalab/openface), [DeepFace](https://github.com/RiweiChen/DeepFace) and [HyperFace](https://arxiv.org/pdf/1603.01249.pdf). To make things fun, I will add the option to add your own face to the database so you can be identified by Kat.

### Emotion

* __Facial emotions__ <br>
We will use a Deep Neural Network model made in Tensorflow. The training will be done using the [Radboud Faces Database](http://www.socsci.ru.nl:8180/RaFD2/RaFD?p=main) or [Paul Ekman's database](https://www.paulekman.com/).

* __Sentiment Analysis__ <br>
A [research paper](http://www.aclweb.org/anthology/D16-1024) from Peking University presented a way to do this using a Long Short Term Memory network. For this to work, I will use this [database](https://snap.stanford.edu/data/web-Amazon.html) that contains 35 million Amazon reviews. I will try to keep an eye out for ways to make this more efficient.

### Higher mental functions
I can not fathom out what it would take for an AI to have a judgement of its own.

This does indeed raise several questions: "What is __consciousness__? How come humans aquire it after a certain age?"

If we are to say that we, as humans, are capable of becoming self-conscious because we try to compare ourselves to someone else and improve our status, what stops a bot from doing the same thing? If we try to look at it from the same perspective that we view children, should we believe that an AI will aquire this trait on its own by learning about the world? How do we know that it understands what it is learning?

This implies much more than what I indicated earlier. Planning, creativity and who knows what else would be required to have a starting point. Until then, we can only speculate the answer.

## Body
Work in progress.

## Drawbacks
The goal of this project is to run all of the previously mentioned systems at once. This means that a lot of RAM and VRAM is needed to process visual cues, text and body functions.

Using cloud computing, for now, is out of the question. 

## [Bucketlist](https://github.com/takusui/Kat.ai/wiki/Bucketlist)
 
## Author notes

This will be a long journey. I created this repository with the intention to keep track of my work and hopefully become more motivated with this project. I don't know how much I can do in the following months because I have some exams to take care of, but I believe that I will start working consistently on this project after graduating this year from highschool. I'm open to new ideas and hopefully, with the experience I will gather in the next few years and with the development of open source technologies that I could use, I can bring Kat to a build that is working decently.

Of course, I can't do all of this on my own. I am looking for other people interested in developing the next-gen virtual bots. If you would like to contribute, please leave a message in the Issues tab.

More info can be found on the wiki.
