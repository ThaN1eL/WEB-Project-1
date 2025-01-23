document.addEventListener('alpine:init', () => {
    Alpine.data('products', () => ({
       items: [
          { id: 1, name: 'Omnipotence Staff', img:'product2.png', price: 1000 },
          { id: 2, name: 'Megumin Hat', img: 'product3.png', price: 300},
          { id: 3, name: 'Omnipotence Grimoire', img: 'product1.png', price: 5555},
          { id: 4, name: 'Holy Wand Court Emblem', img: 'product5.png', price: 2250}
        ]
        
    }));
});