from flask import Flask, render_template
from datetime import datetime

current_year = datetime.now().year

app = Flask(__name__, template_folder='templates', static_folder='static')



cities = {
    'ufa': {
        'name': 'Уфа',
        'places': [
            {'name': 'Башкирский государственный театр оперы и балета', 'image': 'https://upload.wikimedia.org/wikipedia/commons/f/f8/%D0%91%D0%B0%D1%88%D0%BA%D0%B8%D1%80%D1%81%D0%BA%D0%B8%D0%B9_%D1%82%D0%B5%D0%B0%D1%82%D1%80_%D0%BE%D0%BF%D0%B5%D1%80%D1%8B_%D0%B8_%D0%B1%D0%B0%D0%BB%D0%B5%D1%82%D0%B0.JPG'},
            {'name': 'Парк Победы', 'image': 'https://upload.wikimedia.org/wikipedia/commons/3/3b/%D0%9F%D0%B0%D1%80%D0%BA_%D0%9F%D0%BE%D0%B1%D0%B5%D0%B4%D1%8B_%28%D0%B0%D0%BB%D0%BB%D0%B5%D1%8F%29.jpg'},
            {'name': 'Площадь Салавата Юлаева', 'image': 'https://ufa.richotels.ru/97.jpg'},
            {'name': 'Парк mega', 'image': 'https://mega.ru/upload/medialibrary/405/40550217110e77448f078bb2a5a562da.jpg'},
            {'name': 'Аллея современной скульптуры ArtTerria', 'image': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2b/81/fc/bf/caption.jpg?w=1400&h=-1&s=1'},
            {'name': 'Театральный сквер, фонтан «Семью девушек»', 'image': 'https://museum-ufa.ru/wp-content/uploads/2024/03/04-fontan-sem-devushek.jpg'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/Уфа'
    },
    'durtuli': {
        'name': 'Дюртюли',
        'places': [
            {'name': 'Набережная', 'image': 'https://th.bing.com/th/id/OIP.81-GvBVMqEsTcMcWfNSjQAHaE7?w=108&h=108&c=1&bgcl=029841&r=0&o=7&dpr=1.3&pid=ImgRC&rm=3'},
            {'name': 'Дом культуры', 'image': 'https://th.bing.com/th/id/OIP.epgUyWeJthtTlshQ8w0UyQHaEK?w=322&h=181&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3'},
            {'name': 'Парк "Зерно"', 'image': 'https://avatars.mds.yandex.net/get-altay/16482798/2a000001989b21cf45ee0cd9ee9e43d37393/XXL_height'},
            {'name': 'Парк Матросова', 'image': 'https://avatars.mds.yandex.net/get-altay/5457654/2a0000017d47e8c16fc3f007b6d4f2c808e3/XXL_height'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/Дюртюли'

        
    },
    'sterlitamak': {
        'name': 'Стерлитамак',
        'places': [
            {'name': 'Городской парк культуры и отдыха', 'image': 'https://avatars.mds.yandex.net/get-altay/14014620/2a0000019255720b5f9c6fca0986384ca5e2/XXL_height'},
            {'name': 'Набережная Стерли', 'image': 'https://th.bing.com/th/id/OIP.pvrgjMqfAlRqlxjZH76ZFQHaE6?w=108&h=108&c=1&bgcl=798b6d&r=0&o=7&cb=ucfimg1&dpr=1.3&pid=ImgRC&rm=3&ucfimg=1'},
            {'name': 'Музей истории города Стерлитамак', 'image': 'https://museumstr.ru/img/slid1.png'},
            {'name': 'Гора Юрактау', 'image': 'https://th.bing.com/th/id/ODL.781e117b6dfc7e0a0e9f475f05bf33f8?w=312&h=200&c=12&rs=1&pcl=faf9f7&o=6&cb=ucfimg1&dpr=1.3&pid=AlgoBlockDebug&ucfimg=1'},
            {'name': 'Театр драмы', 'image': 'https://teatrygoroda.ru/assets/files/image-547.jpg'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D0%B5%D1%80%D0%BB%D0%B8%D1%82%D0%B0%D0%BC%D0%B0%D0%BA',
    },
    'salavat': {
        'name': 'Салават',
        'places': [
            {'name': 'Музей истории города Салават', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/95/Museum_3_salavat.jpg/330px-Museum_3_salavat.jpg'},
            {'name': 'Горнолыжный центр «Спутник» (Зирган-Тау)', 'image': 'https://tur-ray.ru/wp-content/uploads/2022/06/gornolyzhnyy-tsentr-sputnik-zirgan-tau.jpg'},
            {'name': 'Парк культуры и отдыха', 'image': 'https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Parksalavat.jpg/1280px-Parksalavat.jpg'},
            {'name': 'Набережная', 'image': 'https://tur-ray.ru/wp-content/uploads/2022/06/naberezhnaya-dobro-pozhalovat.jpg'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%A1%D0%B0%D0%BB%D0%B0%D0%B2%D0%B0%D1%82',
    },
    'oktyabrsky': {
        'name': 'Октябрьский',
        'places': [
            {'name': 'Фонтанный сквер', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/10/fontannyy-skver.jpg'},
            {'name': 'Парк Победы', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/10/park-pobedy-2.jpg'},
            {'name': 'Парк им. Ю.А. Гагарина', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/10/park-im.-yu.a.-gagarina.jpg'},
            {'name': 'Звёздный парк', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/10/zvezdnyy-park.jpg'},
            {'name': 'Муллинские карьеры', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/10/mullinskie-karery.jpg'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%9E%D0%BA%D1%82%D1%8F%D0%B1%D1%80%D1%8C%D1%81%D0%BA%D0%B8%D0%B9_(%D0%B3%D0%BE%D1%80%D0%BE%D0%B4)',
    },
    'neftyekamsk': {
        'name': 'Нефтекамск',
        'places': [
            {'name': 'Экопарк «Озеро Светлое»', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/05/ekopark-ozero-svetloe.jpg'},
            {'name': 'Озеро «Полуденка»', 'image': 'https://tur-ray.ru/wp-content/uploads/2023/05/ozero-poludenka.jpg'},
            {'name': 'Тропа здоровья', 'image': 'https://static.tildacdn.com/tild3366-6431-4261-a230-333134663938/1__.jpg'},
            {'name': 'парк культуры и отдыха', 'image': 'https://sun9-8.userapi.com/s/v1/ig2/_E133wDn6GiWElQBXdymQ4Lltpmjsw6lo-eZeetNcuCH5tBIT0TVbxyOYVqTIp0AuHOiGgafdViaWMv0PRqT82C5.jpg?quality=95&as=32x21,48x32,72x48,108x72,160x107,240x160,360x240,480x320,540x360,640x426,720x479,940x626&from=bu&cs=940x0'},
            ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%9D%D0%B5%D1%84%D1%82%D0%B5%D0%BA%D0%B0%D0%BC%D1%81%D0%BA',
    },
    'beloretsk': {
        'name': 'Белорецк',
        'places': [
            {'name': 'Южно-Уральский государственный природный заповедник', 'image': 'https://tur-ray.ru/wp-content/uploads/2021/04/YUzhno-Uralskiy-gosudarstvennyy-prirodnyy-zapovednik.jpg'},
            {'name': 'Аллея героев', 'image': 'https://tur-ray.ru/wp-content/uploads/2021/04/Alleya-geroev.jpeg'},
            {'name': 'Горнолыжный центр Мраткино', 'image': 'https://tur-ray.ru/wp-content/uploads/2021/04/Gornolyzhnyy-tsentr-Mratkino.jpg'},
            {'name': 'Капова пещера', 'image': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/08/78/77/62/caption.jpg?w=1000&h=-1&s=1'},
            {'name': 'Природный парк Иремель', 'image': 'https://dynamic-media-cdn.tripadvisor.com/media/photo-o/0c/c9/a5/b8/caption.jpg?w=1000&h=800&s=1'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%91%D0%B5%D0%BB%D0%BE%D1%80%D0%B5%D1%86%D0%BA',
    },
    'ishimbay': {
        'name': 'Ишимбай',
        'places': [
            {'name': 'Набережная', 'image': 'https://tur-ray.ru/wp-content/uploads/2025/04/naberezhnaya-belskiy-pkio.webp'},
            {'name': 'Ишимбайский историко-краеведческий музей', 'image': 'https://cdn.ruwiki.ru/ruwiki/files/thumb/7/7c/%D0%98%D1%88%D0%B8%D0%BC%D0%B1%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%BA%D0%BE-%D0%BA%D1%80%D0%B0%D0%B5%D0%B2%D0%B5%D0%B4%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9.jpg/274px-%D0%98%D1%88%D0%B8%D0%BC%D0%B1%D0%B0%D0%B9%D1%81%D0%BA%D0%B8%D0%B9_%D0%B8%D1%81%D1%82%D0%BE%D1%80%D0%B8%D0%BA%D0%BE-%D0%BA%D1%80%D0%B0%D0%B5%D0%B2%D0%B5%D0%B4%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9_%D0%BC%D1%83%D0%B7%D0%B5%D0%B9.jpg'},
            {'name': 'Лесопарк им. Полякова', 'image': 'https://avatars.mds.yandex.net/get-altay/941278/2a000001886d79c806f4bd0ec3f1d6efccb3/XXXL'},
            {'name': 'Парк культуры и отдыха имени М. Гафури', 'image': 'https://th.bing.com/th/id/OIP.fJR2CTaeAQb89nbkgsxsGwHaE8?w=137&h=108&c=7&qlt=90&bgcl=e28007&r=0&o=6&cb=ucfimg1&dpr=1.3&pid=13.1&ucfimg=1'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%98%D1%88%D0%B8%D0%BC%D0%B1%D0%B0%D0%B9',
    },
    'kumertau': {
        'name': 'Кумертау',
        'places': [
            {'name': 'Парк культуры и отдыха им. Ю.А. Гагарина', 'image': 'https://tur-ray.ru/wp-content/uploads/2025/09/park-kultury-i-otdyha-im.-yu.a.-gagarina-1024x768.webp'},
            {'name': 'Историко-краеведческий музей', 'image': 'https://img.exponat-online.ru/large/museum/77/8608-0.jpg'},
            {'name': 'Парк культуры и отдыха имени Юрия Гагарина', 'image': 'https://avatars.mds.yandex.net/get-altay/15395175/2a00000197d0d900aa6901447e28c59d3a06/XXXL'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%9A%D1%83%D0%BC%D0%B5%D1%80%D1%82%D0%B0%D1%83',
    },
    'agidel': {
        'name': 'Агидель',
        'places': [
            {'name': 'Зоопарк. Саузово.', 'image': 'https://nashural.ru/assets/uploads/image003-100.jpg'},
            {'name': 'Световой фантан', 'image': 'https://nashural.ru/assets/uploads/image007-84.jpg'},
            {'name': 'Набережная', 'image': 'https://th.bing.com/th/id/OIP.be06bX5PT_5BI_hcsqDnugHaEK?w=108&h=108&c=1&bgcl=460db9&r=0&o=7&cb=ucfimg1&dpr=1.3&pid=ImgRC&rm=3&ucfimg=1'},
        ],
        'wiki_link': 'https://ru.wikipedia.org/wiki/%D0%90%D0%B3%D0%B8%D0%B4%D0%B5%D0%BB%D1%8C',
    },
}





@app.route('/')
def home():
    template = """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Путешествия по Башкортостану</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">

    </head>
    <body>
        <header>
            <h1>Добро пожаловать в мир путешествий по Башкортостану!</h1>
        </header>
        <h1>Выберите город, чтобы увидеть интересные места!</h1>
        <ul class="city-list">
            <li><a href="ufa">Уфа</a></li>
            <li><a href="durtuli">Дюртюли</a></li>
            <li><a href="sterlitamak">Стерлитамак</a></li>
            <li><a href="salavat">Салават</a></li>
            <li><a href="oktyabrsky">Октябрьский</a></li>
            <li><a href="neftyekamsk">Нефтекамск</a></li>
            <li><a href="beloretsk">Белорецк</a></li>
            <li><a href="ishimbay">Ишимбай</a></li>
            <li><a href="kumertau">Кумертау</a></li>
            <li><a href="mezygorye">Межгорье</a></li>
            <li><a href="agidel">Агидель</a></li>
        </ul>

        <footer>
            <div class="footer-content">
                <p>&copy; {{ year }} Путешествия по Башкортостану.</p>
                <div class="footer-links">
                    <a href="/about">О нас</a> | <a href="/contacts">Контакты</a> | <a href="/privacy">Политика конфиденциальности</a>
                </div>
                <div class="social-icons">
                    <a href="#" title="VK">📘</a> <a href="#" title="Telegram">💬</a> <a href="#" title="Instagram">📷</a>
                </div>
            </div>
        </footer>
    </body>
    </html>
    """
    return render_template_string(template, year=current_year)

def generate_city_template(city_key):
    city = cities[city_key]
    places_html = "".join(f"<li><img src='{place['image']}' alt='{place['name']}' style='width:200px;'> {place['name']}</li>" for place in city['places'])
    template = f"""
    
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>{city['name']}</title>
        <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">

    </head>
    <body>
        <header>
            <h1>Добро пожаловать в мир путешествий по Башкортостану!</h1>
        </header>
        <div class="places">
            <h2>{city['name']}</h2>
            <ul>{places_html}</ul>
            <a href="{city['wiki_link']}" target="_blank">Читай подробнее об этом городе на википедии</a>  
        

        <a href="/" class="back-btn">Назад</a>
    </body>
    </html>
    """
    return template





@app.route('/ufa')
def ufa():
    return render_template(generate_city_template('ufa.html'))

@app.route('/durtuli')
def durtuli():
    return render_template(generate_city_template('durtuli'))

@app.route('/sterlitamak')
def sterlitamak():
    return render_template(generate_city_template('sterlitamak'))

@app.route('/salavat')
def salavat():
    return render_template(generate_city_template('salavat'))

@app.route('/oktyabrsky')
def oktyabrsky():
    return render_template(generate_city_template('oktyabrsky'))

@app.route('/neftyekamsk')
def neftyekamsk():
    return render_template(generate_city_template('neftyekamsk'))

@app.route('/beloretsk')
def beloretsk():
    return render_template(generate_city_template('beloretsk'))
    
@app.route('shimbay')
def ishimbay():
    return render_template(generate_city_template('ishimbay'))

@app.route('/kumertau')
def kumertau():
    return render_template(generate_city_template('kumertau'))


@app.route('/agidel')
def agidel():
    return render_template(generate_city_template('agidel'))











