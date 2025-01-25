document.addEventListener('alpine:init', () => {
    Alpine.data('products', () => ({
       items: [
          { id: 1, name: 'Omnipotence Staff', img:'product2.png', price: 1000 },
          { id: 2, name: 'Megumin Hat', img: 'product3.png', price: 300},
          { id: 3, name: 'Omnipotence Grimoire', img: 'product1.png', price: 5555},
          { id: 4, name: 'Holy Wand Court Emblem', img: 'product5.png', price: 2250}
        ]
        
    }));

    Alpine.store('cart', {
        items: [],
        total: 0,
        quantity: 0,
        add(newItem) {
            // check if there is any duplicated item in cart
            const cartItem = this.items.find((item) => item.id === newItem.id);

            // if cart still empty 
            if(!cartItem){
                this.items.push({...newItem, quantity: 1, total: newItem.price });
                this.quantity++;
                this.total += newItem.price;
            } else {
                //if theres a items, check same item or no
                this.items = this.items.map((item) => {
                //if item is different
                if (item.id !== newItem.id) {
                    return item;
                } else {
                    //if item is available, add quantity and total price
                    item.quantity++;
                    item.total = item.price * item.quantity;
                    this.quantity++;
                    this.total += item.price;
                    return item;
                }
                });
            }
        },
        remove(id) {
            //remove item based on the id
            const cartItem = this.items.find((item) => item.id === id);

            //if item more than 1
            if(cartItem.quantity >1) {
                this.items = this.items.map((item) => {
                    if(item.id !== id){
                        return item;
                    } else {
                        item.quantity--;
                        item.total = item.price * item.quantity;
                        this.quantity--;
                        this.total -= item.price;
                        return item;
                    }
                });
            } else if (cartItem.quantity === 1) {
                this.items = this.items.filter((item) => item.id !== id);
                this.quantity--;
                this.total -= cartItem.price;
            }
        },
    });
});


//Convert to USD
const USD = (number) => {
    return new Intl.NumberFormat('usa-EN', {
        style: 'currency',
        currency: 'USD',
        minimumFractionDigits: 2,
    }).format(number);
};