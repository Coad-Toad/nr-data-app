import streamlit as st
import requests
import components as com
import functions as fu


nrdb_card = "https://netrunnerdb.com/en/card/"
nrdb_search = "https://api-preview.netrunnerdb.com/api/v3/public/cards?filter[search]="
nrdbapi_card = "https://api-preview.netrunnerdb.com/api/v3/public/printings/"


text_input = st.text_input(
    "",
    type="search",
    placeholder="Search for Netrunner cards"
)

if text_input:
    try:
        search = fu.load_data(nrdb_search + text_input)
    except:
        st.error(f"Failed to load data: {requests.exceptions.RequestException}")

    results = []

    count = search["meta"]["stats"]["total"]["count"]

    if count == 1:
        st.info(f"found " + str(count) + " cards.")
        image = search["data"][0]["attributes"]["latest_printing_images"]["nrdb_classic"]["large"]
        st.image(image,
        caption=search["data"][0]["attributes"]["stripped_title"])
        
    if count > 1:
        st.info(f"found " + str(count) + " cards.")
        imageurls = []
        captions = []
        idx = 0
        col1, col2, col3 = st.columns(3)
        for _ in range(count):
            while idx < count:
                image = search["data"][idx]["attributes"]["latest_printing_images"]["nrdb_classic"]["medium"]
                caption = search["data"][idx]["attributes"]["stripped_title"]

                imageurls.append(image)
                captions.append(caption)

                if idx % 3 == 0:
                    with col1:
                        st.image(image)

                if idx % 3 == 1:
                    with col2:
                        st.image(image)

                if idx % 3 == 2:
                    with col3:
                        st.image(image)

                idx += 1

carouselcards = [
    "30039",
    "back",
    "34087",
    "21105",
    "01004",
    "35078",
    "11017"
]

carouseldata = {}

# creates an integer to iterate over

for index, cardcode in enumerate(carouselcards):
    carouseldata["card{0}_code".format(index +1)] = cardcode

    if cardcode == "back":
        carouseldata["card{0}_code".format(index +1)] = "35050"
        carouseldata["card{0}_name".format(index +1)] = "Would you like to access?"
        carouseldata["card{0}_image".format(index +1)] = "https://github.com/mtgred/netrunner/blob/master/resources/public/img/nsg-corp.png?raw=true"

    else:

        cardjson = fu.load_data(nrdbapi_card + cardcode)

        carouseldata["card{0}_name".format(index +1)] = cardjson["data"]["attributes"]["stripped_title"]
        carouseldata["card{0}_image".format(index +1)] = cardjson["data"]["attributes"]["images"]["nrdb_classic"]["large"]


com.carousel(carouseldata)