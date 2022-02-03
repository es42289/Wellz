import streamlit as st, pandas as pd, numpy as np, plotly.express as px, streamlit.components.v1 as components, time
# import streamlit.components.v1 as components
from pivottablejs import pivot_ui

st.set_page_config(layout="wide")

dfprd=None

#set title
st.title ('U.S. Well Finder')
#call in paired down well header file
# file='medium_Headers.csv'

# file2='PRD_Directory.csv'
file2='https://github.com/es42289/WellzRepo/raw/master/PRD_Directory.parquet'

#cache the data to eliminate annoying repetitive loading
@st.cache
def load_data():
    data=pd.DataFrame()
    for each in list(range(1,8,1)):
        dft=pd.read_parquet('https://github.com/es42289/WellzRepo/raw/master/medium_Headers_%s.parquet'%each)
        data=pd.concat([data,dft])
    return data
@st.cache
def load_data2():
    dfdir=pd.read_parquet(file2)
    return dfdir

#establish the list of columns we actully care about
cols=['State','Field','Operator Company Name','Reservoir','Production Type','Producing Status','County/Parish','Section',
    'Township','Range','Drill Type','Well/Lease Name','Well Number','Spud Date','API/UWI']
data = load_data()

text1=st.text("Kindly follow the steps below")
st.header('Step #1')
st.text('To plot wells on a map you first have to filter down to 20,000 or less')
st.subheader('How many filters do you want?')
#user selects number of filters they want
filter_num=st.selectbox("No. Filters",[0,1,2,3,4,5,6])
#if statements below are for up to 6 filters
if filter_num==1:
    data = load_data()
    filter1=st.selectbox('Column Filter 1',cols)
    filter12=st.multiselect('Filter Value 1',data[filter1].unique())
    if filter12!=[]:
        data=data[data[filter1].isin(filter12)]
if filter_num==2:
    data = load_data()
    col1, col2 = st.columns(2)
    st.text(data.shape)
    with col1:
        filter1=st.selectbox('Column Filter 1',cols)
        filter12=st.multiselect('Filter Value 1',sorted([str(i) for i in data[filter1].unique()]))
        if filter12!=[]:
            data=data[data[filter1].isin(filter12)]
    with col2:
        filter2=st.selectbox('Column Filter 2',cols)
        filter22=st.multiselect('Filter Value 2',sorted([str(i) for i in data[filter2].unique()]))
        if filter22!=[]:
            data=data[data[filter2].isin(filter22)]
    
if filter_num==3:
    data = load_data()
    col1, col2, col3= st.columns(3)
    with col1:
        filter1=st.selectbox('Column Filter 1',cols)
        filter12=st.multiselect('Filter Value 1',sorted([str(i) for i in data[filter1].unique()]))
        if filter12!=[]:
            data=data[data[filter1].isin(filter12)]
    with col2:
        filter2=st.selectbox('Column Filter 2',cols)
        filter22=st.multiselect('Filter Value 2',sorted([str(i) for i in data[filter2].unique()]))
        if filter22!=[]:
            data=data[data[filter2].isin(filter22)]
    with col3:
        filter3=st.selectbox('Column Filter 3',cols)
        filter32=st.multiselect('Filter Value 3',sorted([str(i) for i in data[filter3].unique()]))
        if filter32!=[]:
            data=data[data[filter3].isin(filter32)]

if filter_num==4:
    data = load_data()
    col1, col2, col3 = st.columns(3)
    with col1:
        filter1=st.selectbox('Column Filter 1',cols)
        filter12=st.multiselect('Filter Value 1',sorted([str(i) for i in data[filter1].unique()]))
        if filter12!=[]:
            data=data[data[filter1].isin(filter12)]
    with col2:
        filter2=st.selectbox('Column Filter 2',cols)
        filter22=st.multiselect('Filter Value 2',sorted([str(i) for i in data[filter2].unique()]))
        if filter22!=[]:
            data=data[data[filter2].isin(filter22)]
    with col3:
        filter3=st.selectbox('Column Filter 3',cols)
        filter32=st.multiselect('Filter Value 3',sorted([str(i) for i in data[filter3].unique()]))
        if filter32!=[]:
            data=data[data[filter3].isin(filter32)]
    with col1:
        filter4=st.selectbox('Column Filter 4',cols)
        filter42=st.multiselect('Filter Value 4',sorted([str(i) for i in data[filter4].unique()]))
        if filter42!=[]:
            data=data[data[filter4].isin(filter42)]

if filter_num==5:
    data = load_data()
    col1, col2, col3 = st.columns(3)
    with col1:
        filter1=st.selectbox('Column Filter 1',cols)
        filter12=st.multiselect('Filter Value 1',sorted([str(i) for i in data[filter1].unique()]))
        if filter12!=[]:
            data=data[data[filter1].isin(filter12)]
    with col2:
        filter2=st.selectbox('Column Filter 2',cols)
        filter22=st.multiselect('Filter Value 2',sorted([str(i) for i in data[filter2].unique()]))
        if filter22!=[]:
            data=data[data[filter2].isin(filter22)]
    with col3:
        filter3=st.selectbox('Column Filter 3',cols)
        filter32=st.multiselect('Filter Value 3',sorted([str(i) for i in data[filter3].unique()]))
        if filter32!=[]:
            data=data[data[filter3].isin(filter32)]
    with col1:
        filter4=st.selectbox('Column Filter 4',cols)
        filter42=st.multiselect('Filter Value 4',sorted([str(i) for i in data[filter4].unique()]))
        if filter42!=[]:
            data=data[data[filter4].isin(filter42)]
    with col2:
        filter5=st.selectbox('Column Filter 5',cols)
        filter52=st.multiselect('Filter Value 5',sorted([str(i) for i in data[filter5].unique()]))
        if filter52!=[]:
            data=data[data[filter5].isin(filter52)]

if filter_num==6:
    data = load_data()
    col1, col2, col3 = st.columns(3)
    with col1:
        filter1=st.selectbox('Column Filter 1',cols)
        filter12=st.multiselect('Filter Value 1',sorted([str(i) for i in data[filter1].unique()]))
        if filter12!=[]:
            data=data[data[filter1].isin(filter12)]
    with col2:
        filter2=st.selectbox('Column Filter 2',cols)
        filter22=st.multiselect('Filter Value 2',sorted([str(i) for i in data[filter2].unique()]))
        if filter22!=[]:
            data=data[data[filter2].isin(filter22)]
    with col3:
        filter3=st.selectbox('Column Filter 3',cols)
        filter32=st.multiselect('Filter Value 3',sorted([str(i) for i in data[filter3].unique()]))
        if filter32!=[]:
            data=data[data[filter3].isin(filter32)]
    with col1:
        filter4=st.selectbox('Column Filter 4',cols)
        filter42=st.multiselect('Filter Value 4',sorted([str(i) for i in data[filter4].unique()]))
        if filter42!=[]:
            data=data[data[filter4].isin(filter42)]
    with col2:
        filter5=st.selectbox('Column Filter 5',cols)
        filter52=st.multiselect('Filter Value 5',sorted([str(i) for i in data[filter5].unique()]))
        if filter52!=[]:
            data=data[data[filter5].isin(filter52)]
    with col3:
        filter6=st.selectbox('Column Filter 6',cols)
        filter62=st.multiselect('Filter Value 6',data[filter6].unique())
        if filter62!=[]:
            data=data[data[filter6].isin(filter62)]

#report the number of rows after filtering
st.title('# of rows: %s' %'{:,}'.format(data.shape[0]))
data=data.fillna(0)
st.text("")
col1, col2 = st.columns(2)
with col1:
    #user chooses how map is colored
    colorby=st.selectbox('Choose Map Color By Property',cols)
with col2:
    map_style=st.radio('Choose Map Style',['Satellite','Topographic'])
if st.button('Map Data'):

    row_count=st.text('# Rows: %s'%data.shape[0])
    if data.shape[0]<=15000:
        fig = px.scatter_mapbox(data, lat='Surface Latitude (WGS84)', lon='Surface Longitude (WGS84)', size=[5 for i in data.index], size_max=10, height=600,
                            hover_data=cols,color=colorby)
        if map_style == 'Topographic':
            fig.update_layout(mapbox_style="open-street-map")
        else:
            fig.update_layout(mapbox_style="white-bg",mapbox_layers=[{"below": 'traces',"sourcetype": "raster","sourceattribution": "United States Geological Survey",
            "source": ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"]}])

        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

        st.plotly_chart(fig, use_container_width=True)
        # t = pivot_ui(data)
        # with open(t.src) as t:
        #     components.html(t.read(), width=900, height=1000, scrolling=True)
    else:
        st.text('Need less than 15,000 wells to map')
        pass

if st.button('Retrieve Production History'):
    start=time.time()
    if data.shape[0]<=15000:
        with st.spinner('Extracting data from database...just a second'):
            fig = px.scatter_mapbox(data, lat='Surface Latitude (WGS84)', lon='Surface Longitude (WGS84)', size=[5 for i in data.index], size_max=10, height=600,
                                hover_data=cols,color=colorby)
            if map_style == 'Topographic':
                fig.update_layout(mapbox_style="open-street-map")
            else:
                fig.update_layout(mapbox_style="white-bg",mapbox_layers=[{"below": 'traces',"sourcetype": "raster","sourceattribution": "United States Geological Survey",
                "source": ["https://basemap.nationalmap.gov/arcgis/rest/services/USGSImageryOnly/MapServer/tile/{z}/{y}/{x}"]}])

            fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

            st.plotly_chart(fig, use_container_width=True)
            dfdir=load_data2()

            #random well sample for testing
            wells=data['API/UWI'].unique().tolist()
            wells=[i for i in wells if i>0]

            #slice directory to well list
            dfdir=dfdir[dfdir['API'].isin(wells)].drop(['Unnamed: 0'],axis=1)
            #put chunks into list for looping
            chunks=dfdir['Index File'].unique().tolist()
            chunks=list(set([100*(i//100) for i in chunks ]))
            print('chunks: %s'%len(chunks))
            #iniitalize blank df for compiling
            dfprd=pd.DataFrame()
            # cycle through chunks and slice each to well list
            for chunk in chunks:
                # file='downloads/PRD/parquet/chunkier/pchunk'+str(int(chunk+100))+'.parquet'
                file='https://github.com/es42289/WellzRepo/raw/master/pchunk'+str(int(chunk+100))+'.parquet'        
                dft=pd.read_parquet(file)
                dft=dft[dft['API/UWI'].isin(wells)]
                dfprd=pd.concat([dfprd,dft])

            def convert_df(df):
                return df.to_csv().encode('utf-8')
            dfprdcsv=convert_df(dfprd)
            
            st.text(time.time()-start)
            st.download_button('Download PRD History',dfprdcsv,file_name='PRD.csv',mime='text/csv')
        st.success('Done!..click the download button below to save the data')
    else:
        st.subheader("Its best to download less than 20,000 wells")
if dfprd is not None:
    dfprd_cum=dfprd.groupby('Monthly Production Date').agg(['sum','count']).reset_index()
    # dfprd_cum['Monthly Production Date']=pd.to_datetime(dfprd_cum['Monthly Production Date'])
    # st.table(dfprd_cum)
    dfprd_cum=pd.DataFrame({'Monthly Production Date':dfprd_cum['Monthly Production Date'].tolist(),'Monthly Oil':dfprd_cum['Monthly Oil','sum'].tolist(),'Well Count':dfprd_cum['Monthly Oil','count'].tolist()})
    # fig = px.line(dfprd, x="Monthly Production Date", y="Monthly Oil", title='Monthly Oil', color='API/UWI', markers=True)
    # st.plotly_chart(fig, use_container_width=True)
    fig = px.line(dfprd_cum, x="Monthly Production Date", y="Monthly Oil", title='Cum Monthly Oil', markers=True)
    fig2= px.bar(dfprd_cum,x='Monthly Production Date',y='Well Count')
    st.plotly_chart(fig, use_container_width=True)
    st.plotly_chart(fig2, use_container_width=True)
    st.table(dfprd_cum)



