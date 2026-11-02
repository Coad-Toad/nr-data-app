import streamlit as st

def carousel(carouseldata):
    carousel = st.components.v2.component(
        name="carousel",
        html="""<div class="homepage-collage">
                    <div class="homepage-collage-cards">
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card1_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card1_code"] + """">
                            <img class="card" alt=""" + carouseldata["card1_name"] + """ title=""" + carouseldata["card1_name"] + """ src=""" + carouseldata["card1_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card2_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card2_code"] + """">
                            <img class="card" alt=""" + carouseldata["card2_name"] + """ title=""" + carouseldata["card2_name"] + """ src=""" + carouseldata["card2_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card3_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card3_code"] + """">
                            <img class="card" alt=""" + carouseldata["card3_name"] + """ title=""" + carouseldata["card3_name"] + """ src=""" + carouseldata["card3_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card4_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card4_code"] + """">
                            <img class="card" alt=""" + carouseldata["card4_name"] + """ title=""" + carouseldata["card4_name"] + """ src=""" + carouseldata["card4_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card5_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card5_code"] + """">
                            <img class="card" alt=""" + carouseldata["card5_name"] + """ title=""" + carouseldata["card5_name"] + """ src=""" + carouseldata["card5_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card6_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card6_code"] + """">
                            <img class="card" alt=""" + carouseldata["card6_name"] + """ title=""" + carouseldata["card6_name"] + """ src=""" + carouseldata["card6_image"] + """>
                        </a>
                        <a data-track="{&quot;category&quot;:&quot;Homepage&quot;,&quot;action&quot;:&quot;Navigate&quot;,&quot;label&quot;:&quot;""" + carouseldata["card7_name"] + """&quot;}" href="https://netrunnerdb.com/en/card/""" + carouseldata["card7_code"] + """">
                            <img class="card" alt=""" + carouseldata["card7_name"] + """ title=""" + carouseldata["card7_name"] + """ src=""" + carouseldata["card7_image"] + """>
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
    return carousel()