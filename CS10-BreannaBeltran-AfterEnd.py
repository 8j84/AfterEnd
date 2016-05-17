#MAKE A SCORE SYSTEM FOR THE BEGINING!!!!!!!!

# Will the 'branches = f' ever be relevant? 
import sys
branches = ('f')
#F = Forward. You can only move forward.


def display_options(node):
    print '\nChoose'
    for i,p in enumerate(node['Choices']):
        print '\t%d: "%s"' % (i, p[2])
        
def player_says(destination, text):
    global dialogue_node
    print 'You choose to say: "%s"' % text
    dialogue_node = destination
    
Voice = {
    'Intro' : {
        'Description' : '\x1B[3mI am the Voice. You can call me a narrator of sorts. I am here, but I\'m not here. Does that make sense? Anyway, This is the AfterEnd DEMO. This means, due to time contraints, the full version of AfterEnd is unfinished. In this demo, I will describe the people you will meet, and the places you will see. To quit the game is easy. You just need to press q. Be careful! If you quit, you\'ll have to RESTART THE ENTIRE GAME. THERE IS NO SAVING. Now with that out of the way, let\'s begin.... This woman - who appears to be in her early twenties - looks tired. Her grey eyes are like glass and seem to stare right through you. Her skin is pale, and even though her long black hair is in a ponytail, it still reaches the floor. She gives you a small smile.\x1B[23m \"Hello, my name is Doll. I\'m here to ask you a couple of questions. I mean that IS the only way to actually move along on your journey. So with that, let\'s get started. If you could change something about yourself, what would it be?\"',
        'Choices' : [
            (player_says, 'reply_1', 'My past.'), #+
            (player_says, 'reply_2', 'I wouldn\'t change anything.'), #=
            (player_says, 'reply_3', 'My personality.'), #-
            ]
        },
    'reply_1' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Hmm... Your past... Ok, let\'s move on!\"',
        'Choices' : [
            (player_says, 'reply_4', 'Ok!'),
            ]
        },
    'reply_2' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Really? Nothing at all? Ok, let\'s move on.\"',
        'Choices' : [
            (player_says, 'reply_4', '...K.'),
            ]
        },
    'reply_3' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Hmm...\"',
        'Choices' : [
            (player_says, 'reply_4', '...'),
            ]
        },
    'reply_4' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"What do you like to do?\"',
        'Choices' : [
            (player_says, 'reply_5', 'I like to spend time with my friends and family.'),
            (player_says, 'reply_6', 'I like to sleep. A LOT.'),
            (player_says, 'reply_7', 'I like to be alone.'),
            ]
        },
    'reply_5' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s good!\"',
        'Choices' : [
            (player_says, 'reply_8', 'Thanks.'),
            ]
        },
    'reply_6' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"I wish I could sleep that much.\"',
        'Choices' : [
            (player_says, 'reply_8', 'Meh, I\'m just lazy...'),
            ]
        },
    'reply_7' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s kind of sad actually.\"',
        'Choices' : [
            (player_says, 'reply_8', 'WELL EXCUSE ME.'),
            ]
        },
    'reply_8' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"What is the most important to you?\"',
        'Choices' : [
            (player_says, 'reply_9', 'Family.'),
            (player_says, 'reply_10', 'Friends.'),
            (player_says, 'reply_11', 'Me.'),
            ]
        },
    'reply_9' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Awe, how sweet.\"',
        'Choices' : [
            (player_says, 'reply_12', 'Oh stop it you. :D'),
            ]
        },
    'reply_10' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"It\'s good to have friends.\"',
        'Choices' : [
            (player_says, 'reply_12', 'Yep! Friends are great.'),
            ]
        },
    'reply_11' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Well you\'re just me, me, me. Aren\'t you?\"',
        'Choices' : [
            (player_says, 'reply_12', 'Sure, I guess.'),
            ]
        },
    'reply_12' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"Would you risk being hurt for someone important to you?\"',
        'Choices' : [
            (player_says, 'reply_13', 'Of course!'),
            (player_says, 'reply_14', 'I would have to think about it.'),
            (player_says, 'reply_15', 'No.'),
            ]
        },
    'reply_13' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s really brave of you.\"',
        'Choices' : [
            (player_says, 'reply_16', 'It\'s the right thing to do.'),
            ]
        },
    'reply_14' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"I understand.\"',
        'Choices' : [
            (player_says, 'reply_16', 'That\'s a lot of pressure.'),
            ]
        },
    'reply_15' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s pretty selfish.\"',
        'Choices' : [
            (player_says, 'reply_16', 'It\'s called being smart.'),
            ]
        },
    'reply_16' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"Would you risk being killed for someone important to you?\"',
        'Choices' : [
            (player_says, 'reply_17', 'If it means they\'ll be safe.'),
            (player_says, 'reply_18', 'I don\'t have a good answer.'),
            (player_says, 'reply_19', 'Not a chance.'),
            ]
        },
    'reply_17' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"There aren\'t many people who are willing to do that.\"',
        'Choices' : [
            (player_says, 'reply_20', 'I\'d be willing.'),
            ]
        },
    'reply_18' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"It\'s a very difficult decision.\"',
        'Choices' : [
            (player_says, 'reply_20', 'I\'d be scared.'),
            ]
        },
    'reply_19' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"No second thoughts, huh?\"',
        'Choices': [
            (player_says, 'reply_20', 'I wouldn\'t need to think about it.'),
            ]
        },
    'reply_20' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"How do you feel about people?\"',
        'Choices' : [
            (player_says, 'reply_21', 'I like meeting new people.'),
            (player_says, 'reply_22', 'They don\'t bother me.'),
            (player_says, 'reply_23', 'They annoy me.'),
            ]
        },
    'reply_21' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"It\'s good that you\'re social.\"',
        'Choices' : [
            (player_says, 'reply_24', 'I think it\'s fun.'),
            ]
        },
    'reply_22' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"So you feel indifferent towards others?\"',
        'Choices' : [
            (player_says, 'reply_24', 'Yeah. I guess you could say that.'),
            ]
        },
    'reply_23' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Does EVERYTHING bother you?\"',
        'Choices' : [
            (player_says, 'reply_24', 'Almost everything.'), #FIX ALL OF THE ABOVE LATER. NEEDS ITALICS.
            ]
        },
    'reply_24' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"How do you feel about crowds?\"',
        'Choices' : [
            (player_says, 'reply_25', 'They\'re a little claustrophobic.'),
            (player_says, 'reply_26', 'I\'d  need some personal space.'),
            (player_says, 'reply_27', 'You wouldn\'t catch me in one.'),
            ]
        },
    'reply_25' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"I would have to agree with you.\"',
        'Choices' : [
            (player_says, 'reply_28', 'I\'m glad I\'m not alone.'),
            ]
        },
    'reply_26' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s understandable.\"',
        'Choices' : [
            (player_says, 'reply_28', 'Thanks for understanding.'),
            ]
        },
    'reply_27' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"Hmm... Kind of a shut in, aren\'t ya?\"',
        'Choices' : [
            (player_says, 'reply_28', 'I like it that way.'),
            ]
        },
    'reply_28' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"How would you feel if you were the last person on Earth?\"',
        'Choices' : [
            (player_says, 'reply_29', 'I\'d be lonely...'),
            (player_says, 'reply_30', 'I couldn\'t imagine that.'),
            (player_says, 'reply_31', 'I\'d have the world to myself.'),
            ]
        },
     'reply_29' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"So would I...\"',
        'Choices' : [
            (player_says, 'reply_32', 'Now I\'m sad...'),
            ]
        },
    'reply_30' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"I try not to think about it.\"',
        'Choices' : [
            (player_says, 'reply_32', 'Let\'s not talk about it, yeah?'),
            ]
        },
    'reply_31' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s be a world I wouldn\'t want to live in.\"',
        'Choices' : [
            (player_says, 'reply_32', 'Your loss.'),
            ]
        },
    'reply_32' : {
        'Description' : '\x1B[3mDoll asks you:\x1B[23m\"What would you do if you were lost in the woods?\"',
        'Choices' : [
            (player_says, 'reply_33', 'I\'d look for others.'),
            (player_says, 'reply_34', 'WHO NEEDS A MAP?!'),
            (player_says, 'reply_35', 'It\'s best to stick to one path.'),
            ]
        },
    'reply_33' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"That\'s a good idea.\"',
        'Choices' : [
            (player_says, 'reply_36', 'I think so too.'),
            ]
        },
    'reply_34' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"I DO!\"',
        'Choices' : [
            (player_says, 'reply_36', 'WHO NEEDS A MAP EVEN?!'),
            ]
        },
    'reply_35' : {
        'Description' : '\x1B[3mDoll replies with:\x1B[23m\"You\'re probably right.\"',
        'Choices' : [
            (player_says, 'reply_36', 'For once we agree.'),
            ]
        },
    'reply_36' : {
        'Description' : '\x1B[3mDoll asks:\x1B[23m\"What scares you?\"',
        'Choices' : [
            (player_says, 'reply_37', 'The dark.'),
            (player_says, 'reply_38', 'Irrational things like monsters.'),#reply with "Heh... That's funny.
            (player_says, 'reply_39', 'My future.'),
            ]
        },
    'reply_37' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"You never know what\'s hiding in the dark.\"',
        'Choices' : [
            (player_says, 'reply_40', 'That\'s not what I had in mind, but now I\'m more scared.'),
            ]
        },
    'reply_38' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"Heh... That\'s funny.\"',
        'Choices' : [
            (player_says, 'reply_40', 'Uh... '),
            ]
        },
    'reply_39' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"That\'s something you\'ll have to find out.\"',
        'Choices' : [
            (player_says, 'reply_40', '...'),
            ]
        },
     'reply_40' : {
        'Description' : '\x1B[3mDoll asks:\x1B[23m\"Do you know why you\'re here?\"',
        'Choices' : [
            (player_says, 'reply_41', 'No.'),
            (player_says, 'reply_42', 'Should I?'),
            (player_says, 'reply_43', 'Yes.'),
            ]
        },
    'reply_41' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_44', '...'),
            ]
        },
    'reply_42' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_44', '...'),
            ]
        },
    'reply_43' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_44', '...'),
            ]
        },
    'reply_44' : {
        'Description' : '\x1B[3mDoll asks:\x1B[23m\"Do you know what I am?\"',
        'Choices' : [
            (player_says, 'reply_45', '...What do you mean?'),
            (player_says, 'reply_46', 'No.'),
            (player_says, 'reply_47', 'Of course.'),
            ]
        },
    'reply_45' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_48', '...'),
            ]
        },
    'reply_46' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_48', '...'),
            ]
        },
    'reply_47' : {
        'Description' : '\x1B[3mDoll replies:\x1B[23m\"...\"',
        'Choices' : [
            (player_says, 'reply_48', '...'),
            ]
        },
    'reply_48' : {
        'Description' : '\x1B[With that, we conclude the demo of AfterEnd. Thank you for playing. Plese press q.\x1B[23m',
        'Choices' : [
            (player_says, 'reply_49', 'Press q.'),
            (player_says, 'reply_50', 'Do it.'),
            (player_says, 'reply_51', 'Right now.'),
            ]
        }
            
    

    }
    
dialogue_node = 'Intro'

while True:
    node = Voice[dialogue_node]
    
    print 'Voice: %s' %Voice[dialogue_node]['Description']
    if 'Choices' in node:
        display_options(node)
        
        #ask for input
        response = raw_input('>').strip().lower()
        
        #Quit from user response
        if response in ['q','quit']:
            sys.exit(0)
        
        #move to next node
        try:    
            path = node['Choices'][int(response)]
            function = path[0]
            args = path[1:]
            function(*args)
        except:
            print 'Sorry. That isn\'t a choice.'
    #Quit program
    else: 
        sys.exit(0)