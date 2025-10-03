import streamlit as st

st.set_page_config(page_title="Mandé Restaurant • Menú", page_icon="🌮", layout="wide")

# -------------- THEME / STYLES --------------
st.markdown(
    """
    <style>
    .menu-card {
        padding: 0.9rem 1.0rem;
        border: 1px solid #EEE;
        border-radius: 12px;
        margin-bottom: 0.75rem;
        background: #fff;
        box-shadow: 0 1px 2px rgba(0,0,0,0.04);
    }
    .menu-title {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.2rem;
    }
    .menu-desc {
        color: #555;
        font-size: 0.95rem;
        margin-bottom: 0.25rem;
    }
    .price-pill {
        display: inline-block;
        font-weight: 700;
        padding: 0.12rem 0.55rem;
        border-radius: 999px;
        border: 1px solid #e7e7e7;
        background: #f7f7f7;
        margin-left: 0.35rem;
    }
    .section-h2 {
        margin-top: 0.25rem;
        padding-top: 0.25rem;
        border-top: 4px solid #6C63FF22;
        margin-bottom: 0.25rem;
    }
    .subtle {
        color: #666;
        font-size: 0.9rem;
    }
    .headerbar {
        background: linear-gradient(90deg,#7ed95722,#6c63ff22,#ff658422);
        border: 1px solid #eee;
        border-radius: 12px;
        padding: 0.8rem 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -------------- DATA --------------
food_menu = {
    "Picadera": [
        {
            "name": "Trío",
            "desc": "Guacamole, pico de gallo y hummus. Acompañado de totopos.",
            "price": 18,
        }
    ],
    "Tostadas o Tacos (1 orden)": [
        {
            "name": "Pollo",
            "desc": "Refrito de frijoles, pico de gallo, guacamole y queso Monterrey.",
            "price": 9,
        },
        {
            "name": "Carnita",
            "desc": "Refrito de frijoles, cebolla roja encurtida y cilantro.",
            "price": 9,
        },
        {
            "name": "Camarón (Ceviche)",
            "desc": "Refrito de frijoles, camarones, aguacate del país, cebolla roja encurtida y pico de gallo.",
            "price": 12,
        },
        {
            "name": "Pescado (Ceviche)",
            "desc": "Refrito de frijoles, pescado, aguacate del país, cebolla encurtida y cilantro.",
            "price": 12,
        },
        {
            "name": "Baby Bella (Vegano)",
            "desc": "Salteado de cebolla, zanahoria y baby bella sobre hummus, con cebolla y pepinos encurtidos.",
            "price": 10,
        },
        {
            "name": "Taco Pastor",
            "desc": "Refrito de frijoles, aguacate, cebolla encurtida y cilantro.",
            "price": 9,
        },
        {
            "name": "Fish Taco",
            "desc": "Ensalada de repollo mixto, spicy alioli, aguacate, cebolla encurtida y pescado empanado.",
            "price": 10,
        },
    ],
    "Postre": [
        {
            "name": "Cheesecake Frito",
            "desc": "Acompañado de mantecado, jalea de strawberry y chili flakes.",
            "price": 15,
        }
    ],
}

drinks_menu = {
    "Margaritas": [
        {"name": "Mandé Margarita", "desc": None, "price": 10},
        {"name": "Create Your Margarita", "desc": "Sabores: Coconut, Passion Fruit, Strawberry, Mango, Acerola, Tamarindo, Watermelon, Peach.", "price": 12},
    ],
    "Mojitos": [
        {"name": "Mojito Clásico", "desc": None, "price": 11},
        {"name": "Create Your Mojito", "desc": "Sabores: Acerola, Tamarindo, Watermelon, Peach, Coconut, Passion Fruit, Strawberry, Mango.", "price": 11},
    ],
    "Mandé Cocktails": [
        {"name": "La Pícara", "desc": None, "price": 12},
        {"name": "Mezcalita", "desc": "Add your favorite flavor.", "price": 14},
        {"name": "Red Sangria", "desc": None, "price": 12},
        {"name": "Michelada", "desc": "Beer, tomato juice, hot sauce, lime & Tajín.", "price": 9},
    ],
    "Jugos Naturales": [
        {"name": "Passion Fruit", "desc": None, "price": 6},
        {"name": "Tamarindo", "desc": None, "price": 6},
        {"name": "Orange", "desc": None, "price": 6},
        {"name": "Acerola", "desc": None, "price": 6},
        {"name": "Pink or White Grapefruit", "desc": None, "price": 6},
    ],
    "Beers": [
        {"name": "Medalla", "desc": None, "price": 4},
        {"name": "All Beers", "desc": None, "price": 5},
    ],
}

# -------------- HEADER --------------
col1, col2 = st.columns([1, 3])
with col1:
    st.image("https://raw.githubusercontent.com/simple-icons/simple-icons/develop/icons/taco.svg", width=64)
with col2:
    st.title("Mandé Restaurant")
    st.caption("Isla Verde, Carolina PR")
st.markdown('<div class="headerbar"><b>Menú principal</b> • Tostadas, tacos, y más.  Vegetariano y opciones de mariscos disponibles.</div>', unsafe_allow_html=True)

# -------------- SIDEBAR --------------
st.sidebar.header("Navegación")
section = st.sidebar.radio("Ir a:", ["Comida", "Bebidas"])

def render_section(title: str, items: list, cols=2):
    st.subheader(title, anchor=title.lower().replace(" ", "-"))
    # grid
    if cols <= 1:
        cols_list = [st.container()]
    else:
        cols_list = st.columns(cols)
    # place items alternating in columns
    for i, it in enumerate(items):
        with cols_list[i % cols]:
            with st.container():
                st.markdown('<div class="menu-card">', unsafe_allow_html=True)
                st.markdown(f'<div class="menu-title">{it["name"]} <span class="price-pill">${it["price"]}</span></div>', unsafe_allow_html=True)
                if it.get("desc"):
                    st.markdown(f'<div class="menu-desc">{it["desc"]}</div>', unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)

if section == "Comida":
    for cat, items in food_menu.items():
        render_section(cat, items, cols=2 if len(items) > 1 else 1)

else:
    st.markdown("### Bebidas")
    for cat, items in drinks_menu.items():
        render_section(cat, items, cols=2 if len(items) > 1 else 1)

st.divider()
st.markdown('<span class="subtle">Los precios y artículos pueden cambiar sin previo aviso. Mixed drinks disponibles.</span>', unsafe_allow_html=True)

# -------------- OPTIONAL: SHOW MENU IMAGES IF PRESENT LOCALLY --------------
import os
img_paths = ["/mnt/data/AC27363E-4BED-4807-B6E6-F071D5590AC1.jpeg", "/mnt/data/650BA5DB-D9DC-476D-B124-A2C2C3022BCD.jpeg"]
local_imgs = [p for p in img_paths if os.path.exists(p)]
if local_imgs:
    st.divider()
    st.markdown("#### Fotos del menú (referencia)")
    st.image(local_imgs, caption=[os.path.basename(p) for p in local_imgs])
