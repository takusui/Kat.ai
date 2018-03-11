<img src='https://raw.githubusercontent.com/takusui/Kat.ai/master/git/title-logo.png' height="80">

Kat.ai is a multi-platform chatbot that adapts while talking with you. This project aims to speed up the transition of AI into people's life by providing the user with ease of access. Kat will be able to run in any environment and, by using an adaptable sequence to sequence model, speak any language.

The posibilities are endless when it comes to the customization:
* Add your own 3d or 2d models and backgrounds.
* User made themes.
* Add your own voice bank.
* Implement custom commands.
* Sculpt Kat's personality to match your own or make it the opposite.
* More to come.

## Brain structure
![](https://raw.githubusercontent.com/takusui/Kat.ai/master/git/brain.png)

This project will focus on mimicking the human brain using neural networks.

### Language comprehension
Kat.ai will use a minimally trained sequence-to-sequence model built in Tensorflow to answer your questions.

![](https://raw.githubusercontent.com/takusui/Kat.ai/0e74c223a9b6e5eae9f37110425379dd58e1f4e8/git/seq2seq.png)

The model will try to improve itself by asking questions about words that it hasn't encountered before or by searching their definition on the internet. If one is found, you will be asked to confirm if it is correct.

### Speech
I will focus on the deep generative model of raw audio waveforms made by Google's DeepMind, WaveNet. Check their [website](https://deepmind.com/blog/wavenet-generative-model-raw-audio/) to see some [examples](https://storage.googleapis.com/deepmind-media/pixie/us-english/wavenet-1.wav).

## [Bucketlist](https://github.com/takusui/Kat.ai/wiki/Bucketlist)
 
## Author notes

This will be a long journey. I created this repository with the intention to keep track of my work and hopefully become more motivated with this project. I don't know how much I can do in the following months because I have some exams to take care of, but I believe that I will start working consistently on this project after graduating this year from highschool. I'm open to new ideas and hopefully, with the experience I will gather in the next few years and with the development of open source technologies that I could use, I can bring Kat to a build that is working decently.

My main focus for now is to finish the Android app and move on to the cross-platform one. When I think about what this would look like in its final version, I imagine something like a next-gen Alexa that you can interact with fully. More than that, I want to enable her to learn on her own, like a child that you teach for a while to ride a bike and then take off its training wheels. Let us hope that the singularity will never happen.

More info can be found on the wiki.
