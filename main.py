'''
This is the GUI for the Android version.
Work in progress.
To do:
- make another .png for the chatbox that scales better -- done
- find a way to add messages -- done
- find a way to keep messages
- find a way to add the transition between chat and microphone (one goes
up and one goes down) -- done
- research multi threading for the on_press event. -- done
- Find another way to add the messages in the chatbox. -- done

Current problems:
- post button keeps jumping from its original position -- fixed?
- after deleting text from a new line, a space remains that won't allow the
chat box to go back to its original size -- fixed
- can't change background of the post/ microphone button through function -- fixed
- app freezes when calling the speech script -- removed speech script
- takes too long to respond
- can't make messages sit on different sides -- fixed
'''
from kivy.app import App
from kivy.uix.image import Image
import threading
import sys
import os

sys.path.append('./dependencies')

# import dialogengine as kat
import brain
import data_utils
import seq2seq_model
from six.moves import xrange
import tensorflow as tf
import numpy as np

class Message(Image):
    pass

class KatApp(App):
    def post(self):
        msg = self.root.ids.usrinp.text
        if len(msg) > 0:
            msgbox = Message()
            msgbox.ids.mlab.text = msg
            msgbox.ids.mlab.color = (0, 0, 0)
            msgbox.pos_hint = {'right': 1}
            msgbox.source = './icons/usr_box.png'
            self.root.ids.chatbox.add_widget(msgbox)
            self.root.ids.scrlv.scroll_to(msgbox)
            self.root.ids.usrinp.text = ''

    def resp(self, msg):
        def p():
            if len(msg) > 0:
                # ansr = kat.answer(msg)
                ansr = answersqs(msg)
                ansrbox = Message()
                ansrbox.ids.mlab.text = str(ansr)
                ansrbox.ids.mlab.color = (1, 1, 1)
                ansrbox.pos_hint = {'x': 0}
                ansrbox.source = './icons/ansr_box.png'
                self.root.ids.chatbox.add_widget(ansrbox)
                self.root.ids.scrlv.scroll_to(ansrbox)

        threading.Thread(target=p).start()

_buckets = [(5, 10), (10, 15), (20, 25), (40, 50)]

def create_model(session, forward_only):
    # Create model and initialize or load parameters
    model = seq2seq_model.Seq2SeqModel( gConfig['enc_vocab_size'], gConfig['dec_vocab_size'], _buckets, gConfig['layer_size'], gConfig['num_layers'], gConfig['max_gradient_norm'], gConfig['batch_size'], gConfig['learning_rate'], gConfig['learning_rate_decay_factor'], forward_only=forward_only)

    if 'pretrained_model' in gConfig:
        model.saver.restore(session,gConfig['pretrained_model'])
        return model

    ckpt = tf.train.get_checkpoint_state(gConfig['working_directory'])
    # the checkpoint filename has changed in recent versions of tensorflow
    checkpoint_suffix = ""
    if tf.__version__ > "0.12":
        checkpoint_suffix = ".index"
    if ckpt and tf.gfile.Exists(ckpt.model_checkpoint_path + checkpoint_suffix):
        print("Reading model parameters from %s" % ckpt.model_checkpoint_path)
        model.saver.restore(session, ckpt.model_checkpoint_path)
    else:
        print("Created model with fresh parameters.")
        session.run(tf.global_variables_initializer())
    return model

def answersqs(sentence):
    with graph.as_default(), sess.as_default():
        # Get token-ids for the input sentence.
        token_ids = data_utils.sentence_to_token_ids(tf.compat.as_bytes(sentence), enc_vocab)
        # Which bucket does it belong to?
        bucket_id = min([b for b in xrange(len(_buckets))
                        if _buckets[b][0] > len(token_ids)])
        # Get a 1-element batch to feed the sentence to the model.
        encoder_inputs, decoder_inputs, target_weights = model.get_batch(
            {bucket_id: [(token_ids, [])]}, bucket_id)
        # Get output logits for the sentence.
        _, _, output_logits = model.step(sess, encoder_inputs, decoder_inputs,
                                        target_weights, bucket_id, True)
        # This is a greedy decoder - outputs are just argmaxes of output_logits.
        outputs = [int(np.argmax(logit, axis=1)) for logit in output_logits]
        # If there is an EOS symbol in outputs, cut them at that point.
        if data_utils.EOS_ID in outputs:
            outputs = outputs[:outputs.index(data_utils.EOS_ID)]
        # Print out French sentence corresponding to outputs.
        return " ".join([tf.compat.as_str(rev_dec_vocab[output]) for output in outputs])

if __name__ == "__main__":
    if len(sys.argv) - 1:
        gConfig = brain.get_config(sys.argv[1])
    else:
        # get configuration from seq2seq.ini
        gConfig = brain.get_config()

    graph = tf.Graph()
    sess = tf.Session(graph= graph)

    with graph.as_default(), sess.as_default():
        # Create model and load parameters.
        model = create_model(sess, True)
        model.batch_size = 1  # We decode one sentence at a time.

        # Load vocabularies.
        enc_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d.enc" % gConfig['enc_vocab_size'])
        dec_vocab_path = os.path.join(gConfig['working_directory'],"vocab%d.dec" % gConfig['dec_vocab_size'])

        enc_vocab, _ = data_utils.initialize_vocabulary(enc_vocab_path)
        _, rev_dec_vocab = data_utils.initialize_vocabulary(dec_vocab_path)

    KatApp().run()

