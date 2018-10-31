"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
from botocore.vendored import requests
from json import dumps


# --------------- Helpers that build all of the responses ---------------------

def build_speechlet_response(output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        # 'card': {
        #     'type': 'Simple',
        #     'title': "SessionSpeechlet - " + title,
        #     'content': "SessionSpeechlet - " + output
        # },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior -----------------

def get_welcome_response(session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = session
    speech_output = '''
            Welcome wine lover!
            Start with a winedown overview by saying: overview.
            You can also say: commandments, voting, details, or host prep.
            What would you like to know about?
        '''
    # If the user does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = '''
            Sorry, I did not get that.
            Start with a winedown overview by saying overview.
            You can also say commandments, voting or host prep.
            What would you like to know about?
       '''
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    speech_output = 'Have a nice day!'
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        speech_output, None, should_end_session))


def get_overview(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        Winedown is a dinner party where you invite around 10 of your best foodie friends and eat delicious food, paired with delicious wine. 
        It is a competition, but you'll have fun even if you come in last.
        Each person has to make their own dish and bring their own pairing wine. They get rated on how well they go together.
        There is one winner who gets to pick the theme or rule for the next meeting.
        Dishes get better with time as the group learns from each other. Nothing can beat good food, good wine and good friends.
        Now go schedule your next winedown!! Whahoo!

        For more info, you can say: commandments, voting, details, or host prep.
    '''
    should_end_session = False


    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_details(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        The host will send a calendar invite at least two weeks before the event with a recap of the last episode, the big announcement of the rule of the next meet and ideally a joke.
        The day of, the host will set a long table with some fun decorations, full dinner set and of course, two wine glasses on each seat for whites and reds.
        When all your foodie friends have arrived, they will announce what they brought and a lineup will be set to progress from appetizers to dessert.
        They will now present their dishes and wine one at a time.
        Oven should stay warm and contestants can put their dishes in at any time to be prepared for their turn. They are welcome to use the microwave or the fridge as well.
        For each participant, no food can be tasted until everyone has both food and wine, at which point everyone should cheer.
        After all dishes have been tasted, foodies will vote on their favorite wine, food and paring.
        Pairing will take the trophy home and should be voted for first, second and third place in that category getting four, two and one points respectively.
        Winner of the pairing category gets to come without bringing anything next time and gets to set a rule for the next meet.
        Now go schedule your next winedown!! Whahoo!

        For more info, you can say: commandments, voting, overview, or host prep.
    '''
    should_end_session = False


    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_commandments(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        1. Thou shall cook to win. 
        2. Thou shall use at least three ingredients. 
        3. Thou shall honor the winner's wishes. 
        4. Thou shall arrive on time. 
        5. Thou shall present your dish and wine. 
        6. Thou shall cheers before the first bite of each dish. 
        7. Thou shall not waste food. 
        8. Thou shall not spill wine. 
        9. Thou shall not vote for yourself. 
        10. Thou shall have fun.

        For more info, you can say: overview, voting, details, or host prep.
    '''
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_voting_rules(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        Once all dishes have been tasted, everyone will get a piece of paper and a pen.
        Each participant should vote for Best Wine, Best Food and Best Pairing.
        You can also optionally vote for a random category such as best newbie, best use of theme, most original, etcetera.
        The best paring category must have a first, second and third place on each vote.
        First place on pairing gets four points, second place gets two and third place gets one.
        All votes should be collected in a jar or preferably a small chest. 
        Once all votes are in, the moderator will read them out loud and designated counter will pay close attention and record the results.
        Sometimes counters have had too much wine and miss the count. They should be immediately revoked of their counting duties.
        You can optionally have a mid tally count to add drama.
        Finally once all votes have been read, the final count is announced and the winner is revealed.
        The winner now gets to take the trophy home and sets a rule for the next meeting.

        For more info, you can say: overview, commandments, details, or host prep.
    '''
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_host_preparation(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        Make sure you have forks, knives, spoons, plates, napkins, pen and paper and of course, two wine glasses per seat.
        Have a wine opener in the table as well as water and some fun decorations.
        Don't forget to keep the over warm and make some space in the fridge.
        Have some bowls and extra plates available and clean out the dishwasher.
        Make some space on a side table to put platters after they have been served.
        Then you are ready to go!

        For more info, you can say: overview, voting, details, or commandments.
    '''
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_fallback(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        Sorry, I didn't get that.

        You can say: overview, commandments, voting, details, or host prep.
    '''
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def get_help(intent, session, reprompt_text):
    session_attributes = session
    speech_output = '''
        To learn more about winedown you can say: overview, commandments, voting, details, or host prep.
        What would you like to know about?
    '''
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def sample_api_request(intent, session, reprompt_text):
    # Use this to get data that the user may request with a follow up question
    session_attributes = {}
    json = None
    attribute1 = 'default'
    attribute2 = 'default'

    if 'slots' in intent and 'attribute1' in intent['slots'] and 'value' in intent['slots']['attribute1']:
        x = intent['slots']['attribute1']['value']
        r = requests.get('APIendpoint&Query', timeout=10)
        json = r.json()
        if not json:
            speech_output = '''
                Query did not return any results, try saying...
            '''

            speechlet_res = build_speechlet_response(speech_output, None, True)
            return build_response({}, speechlet_res)

        attribute1_id = json[-1]['attribute1']
        params = {
            'param1': str(attribute1)
        }

        if 'attribute2' in intent['slots'] and 'value' in intent['slots']['attribute2']:
            print("Add more params here")
            attribute2 = "filter text"

        print(params)
        r = requests.get('APIendpoint', params=params, timeout=10)
        json = r.json()

        if not json['attribute1']['attribute2']:
            speech_output = '''
                Query did not return any results, try saying ..."
            '''

            speechlet_res = build_speechlet_response(speech_output, None, True)
            return build_response({}, speechlet_res)
        attribute1 = x
    else:
        r = requests.get('APIendpoint&Query', timeout=10)
        json = r.json()

    result = json['attribute1']['attribute2'][0]

    speech_output = '''
        Info about %s with filter of %s is %s
    ''' % (
        attribute1,
        attribute2,
        result['something']
    )
    should_end_session = False

    session_attributes['something'] = result

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)


def sample_function_using_session(intent, session, reprompt_text):
    #Use this to respond to a follow up question from the user
    something = session['attributes']['something']
    session_attributes = {
        'something': something,
    }
    speech_output = '''
        Give some more info about %s using some initial session api response info such as %d or %d or %d .
    ''' % (
        something['name'],
        something['feature1'],
        something['feature2'],
        something['feature3'],
    )
    should_end_session = False

    speechlet_res = build_speechlet_response(speech_output, reprompt_text, should_end_session)
    return build_response(session_attributes, speechlet_res)

# --------------- Events ------------------

def on_session_started(session_started_request, request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" +
          session_started_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    #print('intent: ' + dumps(request['intent']))


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response(session['sessionId'])


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    reprompt_text = '''
        Sorry I didn't get that. To learn more about winedown you can say: overview, commandments, voting, details, or host prep.
        What would you like to know about?
    '''

    # Dispatch to your skill's intent handlers
    if intent_name == "overview":
        return get_overview(intent, session, reprompt_text)
    elif intent_name == "details":
        return get_details(intent, session,reprompt_text)
    elif intent_name == "commandments":
        return get_commandments(intent, session, reprompt_text)
    elif intent_name == "voting_rules":
        return get_voting_rules(intent, session, reprompt_text)
    elif intent_name == "host_preparation":
        return get_host_preparation(intent, session, reprompt_text)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help(intent, session, reprompt_text)
    elif intent_name == "AMAZON.FallbackIntent":
        return get_fallback(intent, session, reprompt_text)
    elif intent_name in ['AMAZON.CancelIntent', 'AMAZON.StopIntent', 'AMAZON.NoIntent']:
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started(
            {'requestId': event['request']['requestId']},
            event['request'],
            event['session']
        )

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
