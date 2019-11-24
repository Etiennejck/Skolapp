var app = new Vue({
    delimiters: ['[[',']]'],    // le delimiters permet d'utiliser vue js avec Django qui utilise aussi les doubles parenthese
    el: '#app',
    data: {
        message:'vous avez afficher cette page le '+new Date().toLocaleString()
    }
});

//afficher un message
var app2 = new Vue({
   delimiters:  ['[[',']]'],
    el: '#app2',
    data: {
       message: "Hello world !!!!"
    }
});

app2.message = "Hello tout le monde ";

//pour permutter la présence d'un élément (v-if= ...)

var app3 = new Vue({
    el: '#app3',
    data: {
        seen: true
    }
});



//création d'une boucle (v-for= ... in tableau d'orgine)
//pour ajouter on utilise .push()

var app4 = new Vue({
    delimiters:  ['[[',']]'],
   el: '#app4',
   data: {
       todo: [
           {text: 'tomates'},
           {text: 'pommes'},
           {text: 'oranges'},
           {text: 'bananes'},
       ]
   }
});

//Gestion des entrées utilisateurs on utilisera (v-on)

var interaction = new Vue({
    delimiters: ['[[',']]'],
   el: '#interaction',
   data:{
        message: 'Bonjour à tous'
   },
   methods:{
        reverseMessage: function () {
            return this.message.split('').reverse().join('')
        }
   }
});

//ajouter plus 1 a une valeur

var ajouter = new Vue({
    delimiters: ['[[',']]'],
    el: '#ajouter',
    data: {
        nombre: 1
    },
    methods: {
        ajouter1: function () {
            this.nombre += 1
        }
    }
});

//Vue fournit aussi la directive v-model qui fait de la liaison de données bidirectionnelle entre
// les champs d’un formulaire et l’état de l’application. Une simple formalité :

var affichageDina = new Vue({
    delimiters: ['[[',']]'],
    el: '#affichageDina',
    data:{
        letexte:''
    }
});

//Dans Vue, un composant est essentiellement une instance de Vue avec des options prédéfinies.
// Déclarer un composant avec Vue est très simple :

//// Définit un nouveau composant appelé todo-item
// Vue.component('todo-item', {
//   template: '<li>Ceci est une liste</li>'
// })
//
// var app = new Vue(...)

//<ol>
//   <!-- Crée une instance du composant todo-list -->
//   <todo-item></todo-item>
// </ol>
//ensuite on ajoute une 'prop' est un attribut personnalisé

Vue.component('todo-item',{
    props: ['todo'],
    template: '<li>{{todo.text}}</li>'
});

var ListComposant = new Vue({
    el:'#ListComposant',
    data:{
        listCourse: [
            {id: 0, text: 'Lait'},
            {id: 1, text: 'citron'},
            {id: 2, text: 'viande'},
            {id: 3, text: 'playmobile'},
            {id: 4, text: 'salamis'},

        ]
    }
});