
import streamlit as st
import requests
import wikipedia

from streamlit_searchbox import st_searchbox

NRDB_URL = "https://netrunnerdb.com/api/2.0/public/card/"
nrdb_card = NRDB_URL

@st.cache_data

#wikipedia search example
def card_search(searchterm: str) -> list:
    return wikipedia.search(searchterm.lower()) if searchterm else []

selected_card = st_searchbox(
    card_search,
    placeholder="Search wikipedia",
)

if selected_card:
    st.write(f"Selected value: {selected_card}")

def load_data(card):
    response = requests.get(card, timeout=10)
    response.raise_for_status()
    return response.json()

text_input = st.text_input(
    "",
    type="search",
    placeholder="Search for Netrunner cards"
)

if text_input:
    try:
        load_data(NRDB_URL + text_input)
    except:
        st.error(f"Failed to load data: {requests.exceptions.RequestException}")


card1_code = "30039"
card1_json = load_data(nrdb_card + card1_code)
card1 = card1_json["data"][0]

card3_code = "34078"
card3_json = load_data(nrdb_card + card3_code)
card3 = card3_json["data"][0]

card4_code = "21105"
card4_json = load_data(nrdb_card + card4_code)
card4 = card4_json["data"][0]

card5_code = "01004"
card5_json = load_data(nrdb_card + card5_code)
card5 = card5_json["data"][0]

card6_code = "35078"
card6_json = load_data(nrdb_card + card6_code)
card6 = card6_json["data"][0]

card7_code = "11017"
card7_json = load_data(nrdb_card + card7_code)
card7 = card7_json["data"][0]


carousel = st.components.v2.component(
    name="carousel",
    html="""<div class="homepage-collage">
                <div class="homepage-collage-cards">
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card1.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card1_code + """">
                        <img class="card" alt="Cran1.0" title=""" + card1.get("title") + """ src=""" + card1_json["imageUrlTemplate"].replace("{code}", card1_code) + """>
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;Would you like to access?&quot;}" href="https://netrunnerdb.com/en/card/35050">
                        <img class="card" alt="" title="Would you like to access?" src="https://github.com/mtgred/netrunner/blob/master/resources/public/img/nsg-corp.png?raw=true">
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card3.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card3_code + """">
                        <img class="card" alt="Alarm Clock" title=""" + card3.get("title") + """ src=""" + card3_json["imageUrlTemplate"].replace("{code}", card3_code) + """>
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card4.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card4_code + """">
                        <img class="card" alt="" title=""" + card4.get("title") + """ src=""" + card4_json["imageUrlTemplate"].replace("{code}", card4_code) + """>
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card5.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card5_code + """">
                        <img class="card" alt="" title=""" + card5.get("title") + """ src=""" + card5_json["imageUrlTemplate"].replace("{code}", card5_code) + """>
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card6.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card6_code + """">
                        <img class="card" alt="" title=""" + card6.get("title") + """ src=""" + card6_json["imageUrlTemplate"].replace("{code}", card6_code) + """>
                    </a>
                    <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + card7.get("title") + """&quot;}" href="https://netrunnerdb.com/en/card/""" + card7_code + """">
                        <img class="card" alt="" title=""" + card7.get("title") + """ src=""" + card7_json["imageUrlTemplate"].replace("{code}", card7_code) + """>
                    </a>
                </div>
            </div>""",
    css=""".homepage-collage a {
                display: block;
                height: 234px;
                position: absolute;
                -webkit-transform: translateY(0);
                -o-transform: translateY(0);
                transform: translateY(0);
                -webkit-transition: -webkit-transform 0.3s;
                transition: -webkit-transform 0.3s;
                -o-transition: -o-transform 0.3s;
                transition: transform 0.3s;
                transition: transform 0.3s, -webkit-transform 0.3s, -o-transform 0.3s;
                width: 168px
            }

                .homepage-collage a.focus .card {
                    border: 2px solid #8932d9
                }

                .homepage-collage a:hover {
                    -webkit-transform: translateY(-9px);
                    -o-transform: translateY(-9px);
                    transform: translateY(-9px)
                }

                .homepage-collage a:nth-child(1) {
                    left: 0;
                    top: 22px
                }

                .homepage-collage a:nth-child(2) {
                    left: 174px;
                    top: 10px
                }

                .homepage-collage a:nth-child(3) {
                    left: 347px;
                    top: 16px
                }

                .homepage-collage a:nth-child(4) {
                    right: 0;
                    top: 35px
                }

                .homepage-collage a:nth-child(5) {
                    left: 35px;
                    top: 62px
                }

                .homepage-collage a:nth-child(6) {
                    left: 206px;
                    top: 45px
                }

                .homepage-collage a:nth-child(7) {
                    left: 380px;
                    top: 65px
                }

            .homepage-collage img.card {
                -webkit-border-radius: 5% / 3.75%;
                border-radius: 5% / 3.75%;
                height: 100%;
                width: 100%
            }

                .homepage-collage img.card.border-black {
                    -webkit-box-shadow: inset 0 0 3px 3px #000;
                    box-shadow: inset 0 0 3px 3px #000
                }"""
)

carousel()

# popup_image = st.components.v2.component(
#     name="popup_image",
#     html="<img src='" + img_url + "'>",
# )

# popup_image()