import streamlit as st
import time

# input widgets
# media elements - https://samplelib.com/
# sidebar


if(st.sidebar.button('Text elements')):
    st.write('this is write')
    st.write("*****this is magic write*****")
    st.markdown('this is markdown')
    st.title('this is title')
    st.header('this is header')
    st.subheader('this is subheader')
    st.caption('this is caption')
    st.code('this is codeblock')
    st.text('this is text')
    st.divider()
    st.latex('this is latex, (a+b)^2 = a^2 + b^2 + 2ab')
    st.divider()

if(st.sidebar.button('Input Widgets')):
    st.text_input('Name')
    st.number_input('Age')
    st.radio('Gender',['Male','Female'])
    st.selectbox('Graduation',(['Secondary School','BTech','Masters']))
    st.multiselect('Skills',['C','Python','Java','Web','AIML'])
    st.toggle("Interested")
    st.slider('How far are your skillset match',0,100)
    st.date_input("Which date are you available for interview?")
    st.time_input('What is the convenient time to attend interview?')
    st.file_uploader("Upload your updated CV")
    #st.camera_input('Take a picture')
    st.text_area("Any suggestions...!")
    st.checkbox('I Agree')
    st.button('Submit')
    st.link_button('Go to URL','https://www.google.com')
    
if(st.sidebar.button('Media elements')):
    st.image('https://tse4.mm.bing.net/th?id=OIP.kLSHOYrpV909KNS-T_irNQHaEY&pid=Api&P=0&h=180')
    st.audio('https://samplelib.com/lib/preview/mp3/sample-3s.mp3')
    st.video('https://samplelib.com/lib/preview/mp4/sample-5s.mp4')

if(st.sidebar.button('Layouts & containers')):
    with st.expander("open to see more"):
        st.write('Here is the columnwise and tabwise')

    col1,col2,col3,col4 = st.columns(4)
    col1.write('this is col1')
    col2.write('this is col2')
    col3.write('this is col3')
    col4.write('this is col4')

    tab1,tab2,tab3 = st.tabs(['Tab1','Tab2','Tab3'])
    tab1.write('this is tab1')
    tab2.write('this is tab2')
    tab3.write('this is tab3')


    c = st.container()
    c.write('container1')
    c.write('container2')

if st.sidebar.button('ChatInput'):
    st.chat_input('say something')
    

if st.sidebar.button('Status Elements'):
    st.snow()
    st.balloons()

    with st.spinner('Please wait...'):
        time.sleep(2)
    st.success('Done')

    for i in range(10):
        st.progress(i)
    st.success('Done')

    with st.status('Running'):
        time.sleep(2)
    st.success('Done')

    st.toast('congrats',icon='🎉')
   
    st.error('This is error')
    st.warning('This is warning')
    st.info('This is info')
    st.success('This is success')
