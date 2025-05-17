# -----------------------------------------------------------------------------
# init: Transform и Image definitions
# -----------------------------------------------------------------------------

transform Soviet_Captain_Down:
    yoffset 200

transform Soviet_Private_Down:
    zoom 0.6
    yoffset 200

transform Soviet_Doctor_Down:
    zoom 0.5
    yoffset 0

transform Zoom_Transform:
    zoom 1.3
    yoffset 100



# -----------------------------------------------------------------------------
# Init Characters
# -----------------------------------------------------------------------------


# Капитан
image Soviet_Captain = At("images/people/Soviet_Captain.png", Soviet_Captain_Down)
define captain = Character("Капитан Серебров")

# Младший сержант
image Soviet_Private = At("images/people/Soviet_Private.png", Soviet_Private_Down)
define Soviet_Private = Character("Младший сержант Садиков")

# Доктор
image Soviet_Doctor = At("images/people/Soviet_Doctor.png", Soviet_Doctor_Down)
define Soviet_Doctor = Character("Доктор Павлова")



# -----------------------------------------------------------------------------
# Init Backgrounds
# -----------------------------------------------------------------------------


image DugoutBg   = "images/bg/Dugout.png"
image MedblockBg   = "images/bg/Medblock.jpeg"


# -----------------------------------------------------------------------------
# Init Real photoes
# -----------------------------------------------------------------------------

image Stalingrad = "images/photo/stalingrad.jpg"
image Moscow     = "images/photo/moscow.jpg"
image Gitler     = "images/photo/gitler.png"
image Kavkaz     = "images/photo/kavkaz.jpg"


# -----------------------------------------------------------------------------
# Init sketches
# -----------------------------------------------------------------------------


image MainMenuSketch = At("images/sketches/Screensaver.png", Zoom_Transform)
image BeforeAssigmentSketch = At("images/sketches/Before_Assigment.png", Zoom_Transform)



# -----------------------------------------------------------------------------
# ИНИЦИАЛИЗАЦИЯ СТИЛЕЙ
# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------
# ЭКРАН: Информационная боковая панель справа
# -----------------------------------------------------------------------------
screen info_sidebar(text):
    frame:
        background Solid("#222")
        xalign 0.98
        yalign 0.5
        xsize 520
        ysize 0.9
        yfill True
        padding (40, 40)
        vbox:
            spacing 20
            text text style "info_text" xalign 0.5 yalign 0.5
        
init:
    # Стиль для информационного текста
    style info_text is default:
        size 36                    # <— вместо text_size
        color "#ffffff"
        xalign 0.5
        yalign 0.8
        xpadding 40
        ypadding 20

init:
    style main_menu_button_new_text is default:
        font "fonts/PlayfairDisplay-ExtraBold.ttf"
        size 36
        color "#ffde22"  # Желтоватый цвет только для текста кнопки "Новая история"
        text_align 0.5
        hover_color "#ffde22"
        background None
        underline False
        hover_underline True

init:
    style main_menu_button_text is default:
        font "fonts/PlayfairDisplay-ExtraBold.ttf"
        size 36
        color "#ffffff"
        text_align 0.5
        hover_color "#EEE"
        background None
        underline False
        hover_underline True

# Добавим стиль для тени фрейма меню
transform menu_shadow:
    xoffset 8
    yoffset 8
    alpha 0.9

init:
    style main_menu_frame is default:
        padding (30, 30)
        xalign 0.8
        yalign 0.5
        xmaximum 350
        ymaximum 300

# -----------------------------------------------------------------------------
# ЭКРАН: Главное меню
# -----------------------------------------------------------------------------
screen main_menu():
    on "show" action Play("music", "audio/victory.mp3", fadein=3.0)

    add "MainMenuSketch" at truecenter
    frame:
        style "main_menu_frame"
        at menu_shadow
        background Solid("#15151544")
        xalign 0.94
        yalign 0.9
        vbox:
            spacing -18
            align (0.5, 0.5)
            textbutton "Новая история" action Start() style "main_menu_button" text_style "main_menu_button_new_text"
            textbutton "Загрузить" action ShowMenu("load") style "main_menu_button"
            textbutton "Настройки" action ShowMenu("preferences") style "main_menu_button"
            textbutton "Выход" action Quit() style "main_menu_button"
                

# -----------------------------------------------------------------------------
# ЛЕЙБЛ: SPLASHSCREEN
# -----------------------------------------------------------------------------
label splashscreen:
    scene black with fade
    pause 1

    show text "Последний приказ" at truecenter with dissolve
    pause 2
    hide text with dissolve

    stop music fadeout 2.0
    return

# -----------------------------------------------------------------------------
# ЛЕЙБЛ: START
# -----------------------------------------------------------------------------
label start:
    play music "audio/theme.mp3" fadein 3.0
    pause 2.0

    # Первый текст (можем использовать inline-теги или стиль)
    window hide
    show text "Шла осень сорок второго года..." at truecenter with dissolve
    pause 10
    hide screen info_sidebar

    # Москва
    scene Moscow with dissolve
    show screen info_sidebar("После героической победы советских войск под Москвой, вермахт потерял надежду на блицкриг. Советский народ проявил небывалую доблесть, сражаясь за каждый клочок родной земли. Подвиг солдат и тружеников тыла стал символом несгибаемой воли и беспримерного мужества. Люди шли на самопожертвование ради будущего своей страны, не щадя ни сил, ни жизни.") with dissolve
    pause 20
    hide screen info_sidebar

    # Гитлер
    scene Gitler with dissolve
    show screen info_sidebar("Адольф Гитлер сосредоточился на проведении масштабного наступления на юге, стремясь взять под контроль стратегически важные районы, богатые нефтью, и нанести сокрушительный удар по советским войскам, чтобы изменить ход войны в пользу Третьего рейха.") with dissolve
    pause 20
    hide screen info_sidebar

    # Сталинград
    scene Stalingrad with dissolve
    show screen info_sidebar("Его целью стал Сталинград — важнейший промышленный и транспортный узел на Волге, который ещё до войны был одним из центров советской индустриализации, славился своими тракторными и металлургическими заводами и играл ключевую роль в снабжении южных регионов страны.") with dissolve
    pause 20
    hide screen info_sidebar

    # Кавказ
    scene Kavkaz with dissolve
    show screen info_sidebar("Если немцам удастся захватить Сталинград, то дороги на районы Кубани и Кавказа открыты, и гитлеровские войска смогут получить прямой доступ к богатым нефтяным месторождениям, стратегическим портам Чёрного моря и лишить СССР важнейших ресурсов для продолжения войны.") with dissolve
    pause 20
    hide screen info_sidebar

    jump introduction
    return

# -----------------------------------------------------------------------------
# ЛЕЙБЛ: INTRODUCTION — знакомство с героем
# -----------------------------------------------------------------------------
label introduction:

    # Показываем землянку и капитана
    scene DugoutBg with fade
    pause 1.0

    # Включаем инфо-окно и выводим текст
    window show

    # Рассказываем о герое
    "Ты — сержант {i}Николай Сергеев{/i}, солдат 62-й армии."
    "За плечами у тебя — несколько ранений, за одно из них у тебя есть медаль «За отвагу»."
    "Ты вместе с отрядом разведчиков находишься на аванпосту в Сталиграде."
    "{cps=30}Шум артобстрелов не дают ни сна, ни передышки."
    "{cps=30}В детстве ты мечтал стать инженером, поступил в институт, но война изменила планы навсегда."
    "{cps=30}Ты родом из Тулы — металл и огонь кузнецких цехов давно в твоей крови."
    "{cps=30}Под ногами хрустят опавшие листья, а в воздухе висит сырой туман."
    "{cps=30}В землянке пахнет порохом и влажной древесной стружкой."
    "{cps=30}Ты хранишь в кармане пожелтевшее фото семьи и мягкую шапку, которую связала мать."
    "{cps=30}На улице ветер гонит опавшие листья по промокшей земле."

    # Закрываем окно и переходим к следующей сцене
    window hide
    pause 1.0

    # Переход к вступительной реплике капитана или меню выбора
    jump capitan_welcome
    return

# -----------------------------------------------------------------------------
# ЛЕЙБЛ: CAPITAN_WELCOME — знакомство с капитаном
# -----------------------------------------------------------------------------
label capitan_welcome:

    # Показываем фон и капитана
    scene DugoutBg with fade
    show Soviet_Captain at truecenter with dissolve
    window show

    # Диалог капитана
    captain "Здравия желаю, товарищ сержант. "  
    captain "Как поживаешь? Не слишком скучаешь по родному дому?"
    captain "Ха-ха, понимаю. Война — не курорт, но и не всё ещё так плохо: ты пока цел, а значит еще можешь пригодится, кхм..."  
    captain "Как твоя семья? Не слышал? Я то сам давно сирота, лишь сестра была до войны, да погибла под Киевом... не успела, понимаешь?"  
    captain "..."   
    captain "Вот прогоним фашистов, вернешься к семье. Увидишь мать с отцом, и как будто не было этого кошмара."  
    captain "Ладно, что-то я расчувствовался. Надо беречь и силы, и воду, не тратить её на слезы." 
    captain "Ты видел радиста?"  

    menu:
        "(ЛОЖЬ) Нет, не видел.": 
            captain "И больше не увидишь, бляха. Нет его больше. И рации нет. Мы без связи.."
        "(ПРАВДА) Да, видел... Точнее то, что от него осталось.": 
            captain "И рацию тоже разнесло, етить его. Мы без связи.." 

    captain "Ладно, Коля. Задание для тебя есть."
    captain "Сходи к медику и уточни состояние младшего сержанта Садикова. Его ранило, но, говорят, он уже на ногах."
    captain "Приведи его сюда, разговор к вам есть."
    captain "Свободен."

    hide Soviet_Captain with dissolve

    window hide

    # Переход к миссии
    jump medblock


# -----------------------------------------------------------------------------
# ЛЕЙБЛ: MEDBLOCK — сцена в медблоке
# -----------------------------------------------------------------------------
label medblock:

    # Показываем фон медблока
    scene MedblockBg with fade
    play sound "effects/door_open.mp3"
    pause 1
    show Soviet_Private at right with dissolve
    pause 1
    window show

    # Диалог младшего сержанта Садикова (не менее 20 реплик)
    Soviet_Private "О, а вот и Николай.. Сегодня прям нет отбоя от гостей. "  
    Soviet_Private "Заходи, поговорим."
    Soviet_Private "Видишь вот, заживаю, как собака дворовая. Ещё бы спину не ломило — цены бы ей не было."  
    Soviet_Private "Доктор колит что-то, чтобы не так сильно ломило.."  
    Soviet_Private "Оно то может и помогает, да после него сны как в цирке или дурном анекдоте."  
    Soviet_Private "Ты зачем пришёл-то? Или просто решил по умирающим походить, настроение поднять?"

    menu:
        "(СПОКОЙНО) Товарищ Капитан зовет нас к себе. Какой-то разговор.":
            Soviet_Private "Разговор, говоришь... Ноги у меня ещё при мне, а вот уверенность где-то там, на поле боя осталась..."   
        "(С ВОЛНЕНИЕМ) Капитан зовет нас к себе. Мне кажется, что-то случилось.":
            Soviet_Private "Связи нет, вот что случилось. Любой бы на его месте запереживал."

    Soviet_Private "Ах, если капитан говорит — значит, надо идти. Даже если у тебя кишки наружу — перевяжут и пошлют дальше."  
    Soviet_Private "Ты, Коль, не обижайся, но отдохнуть бы мне ещё пару дней..."

    # Первое меню выбора
    menu:
        "(СУХО) Понимаю тебя, но иного выхода нет.": 
            Soviet_Private "Ну и правильно. Мне ж не в госпитале валяться, а с вами, родимыми. Как там говорили? ‘Отдохнём в могиле’?"  
        "(ЗАБОТЛИВО) Если хочешь, могу сказать капитану, что ты пока не в форме.": 
            Soviet_Private "Да не, Коль, не надо. Я же не девка хрупкая. Скажешь такое — капитан подумает, что я сдулся."  
            Soviet_Private "А со сдувшимися у него разовор кортокий. Проходили, знаем."  

    # Продолжаем диалог
    Soviet_Private "Без радиста — как без глаз..."  
    Soviet_Private "Вон, раньше Петька был — матерился, как сапожник, но рацию знал, как свою жену."  
    Soviet_Private "Теперь его нет. Ни Петьки, ни рации, может и жены его тоже нет. А мы всё живём."  

    # Второе меню выбора
    menu:
        "(НЕТЕРПЕЛИВО) Пошли, нас ждут.": 
            Soviet_Private "Да, да."  
        "(С ЛЮБОПЫТСТВОМ) Как ты получил ранение?": 
            Soviet_Private "Да я рядом с Петькой был, когда снарядом накрыло."
            Soviet_Private "Очнулся уже тут. По началу ног не чувствовал, но вроде пронесло. Похожу еще, подвигаюсь."
            Soviet_Private "Знаешь, когда земля на тебя давит и кровью пахнет — всё остальное меркнет."  
            Soviet_Private "Но я жив, и значит, ещё пригожусь. Не скажу, что люблю вспоминать, но теперь уже не шевелит..."  

    # Завершающие реплики
    Soviet_Private "Пошли. А то товарищ капитан не любит, когда его заставляют ждать."  
    Soviet_Private "Не хватало бы еще его разозлить."  

    play sound "effects/door_open.mp3"
    pause 1
    show Soviet_Doctor at left with dissolve
    pause 1
    
    Soviet_Doctor "Стойте вы оба!"  
    Soviet_Doctor "Младший сержант Садиков, у вас компрессионный перелом ребра, возможны последствия…"  
    Soviet_Doctor "Я запрещаю вам покидать медблок до полного выздоровления!"  
    Soviet_Private "Ладно вам, товарищ Доктор. Я ценю вашу заботу, но меня вызывает капитан, и я должен идти." 
    Soviet_Doctor "Вы рискуете обострить рану! Вам нужен полный покой."  
    Soviet_Private "Да ладно вам, я не надолго."  
    Soviet_Private "Узнаю, зачем меня вызывает тащ-капитан, вернусь, и буду сутки на пролет лежать, греть место."  
    Soviet_Doctor "…"
    scene black with fade
    window hide
    jump assignment_from_captain


# -----------------------------------------------------------------------------
# ЛЕЙБЛ: assignment_from_captain — Капитан дает задание (АВТОР ВИКТОР КЛЕЙМЕНОВ)
# -----------------------------------------------------------------------------
label assignment_from_captain:
    show BeforeAssigmentSketch with dissolve
    pause 100
    return