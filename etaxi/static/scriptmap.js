ymaps.ready(init);
function init() {
   var myMap = new ymaps.Map("map", {
           center: [55.030204, 82.920430],
           zoom: 3
       }, {
           searchControlProvider: 'yandex#search'
       });

   myMap.geoObjects
       .add(new ymaps.Placemark([56.484645, 84.947649], {
           balloonContentHeader: "Таксопарки в Томске",
           balloonContentBody: ['<a href="https://yandex.ru/maps/-/CDe6eCo7" target="_blank">Торговая, 5</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Иркутский тракт, 77</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Набережная реки Томи, 19/1</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Алтайская, 3</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Иркутский проезд, 1</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Смирнова, 9с3</a><br/>'].join(''),
         //   iconCaption: 'Томск'
           hintContent: 'Томск'
       }, {
           preset: 'islands#icon',
           iconColor: 'red',
           iconCaptionMaxWidth: '200',
       }))
        .add(new ymaps.Placemark([55.030204, 82.920430], {
         balloonContentHeader: "Таксопарки в Новосибирске",
           balloonContent: ['<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Богдана Хмельницкого, 93 корпус 2</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Красный проспект, 220 корпус 87</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Станционная 39/1</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Петухова 67</a><br/>',
           '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Приграничная 1</a><br/>'].join(''),
         //   iconCaption: 'Новосибирск'
           hintContent: 'Новосибирск'
       }, {
           preset: 'islands#icon',
           iconColor: 'red',
           iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([56.010569, 92.852572], {
         balloonContentHeader: "Таксопарки в Красноярске",
         balloonContent: ['<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">ул.Калинина, 68, 2 этаж</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">офис 160 лет Октября, 105ж/1</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Мате Залки 3, офис 2-03</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Авиаторов 3а, 2 этаж</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Забобонова 13, 2 этаж</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Брянская 2-я, 4, офис 301</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Говорова 71, 3 этаж</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Коломенская 17Б</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Полтавская 38/1</a><br/>',
         '<a href="https://yandex.ru/maps/?text=томкс%20 %20" target="_blank">Металлургов 2Р</a><br/>'].join(''),
         // iconCaption: 'Красноярск'
         hintContent: 'Красноярск'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([54.989347, 73.368221], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Омск'
         hintContent: 'Омск'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([55.355198, 86.086847], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Кемерово'
         hintContent: 'Кемерово'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([53.757553, 87.136053], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Новокузнецк'
         hintContent: 'Новокузнецк'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([52.289588, 104.280606], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Иркутск'
         hintContent: 'Иркутск'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([51.834809, 107.584547], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Улан-Удэ'
         hintContent: 'Улан-Удэ'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([57.152985, 65.541227], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Тюмень'
         hintContent: 'Тюмень'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([53.346785, 83.776856], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Барнаул'
         hintContent: 'Барнаул'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       .add(new ymaps.Placemark([56.838011, 60.597474], {
         balloonContent: 'цвет <strong>воды пляжа бонди</strong>',
         // iconCaption: 'Екатеринбург'
         hintContent: 'Екатеринбург'
       }, {
         preset: 'islands#icon',
         iconColor: 'red',
         iconCaptionMaxWidth: '200'
       }))
       
       
}