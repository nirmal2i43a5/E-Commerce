//THis is javascript not jquery look in this link for difference https://learn.onemonth.com/jquery-vs-javascript/
//-----------------------------------------------------------------------------------------------------------------------------------
// var updateBtns = document.getElementsByClassName('update-cart')//point add to cart class 


//         for (i = 0; i < updateBtns.length; i++) {
//             updateBtns[i].addEventListener('click', function(){
//                 var productId = this.dataset.product
                
//                 var action = this.dataset.action
//                 console.log('productId:', productId, 'Action:', action)
//                 console.log('USER:', user)
//                 if (user == 'AnonymousUser'){
//                     console.log('User is not authenticated')
                            
//                 }else{
//                          updateUserOrder(productId, action)
        
                    
//                 }
        
//             });
//         }

//----------------same above logic using jquery----------------------------------

$(document).ready(function(){
    $('.update-cart').on('click',function(){
        var updateBtns = $(this);
        // var productId = this.getAttribute('data-product')
        var productId = this.dataset.product//particular click product id 
        var action = this.dataset.action   //same as using below
        // var action = this.getAttribute('data-action')
        console.log('productId:', productId, 'Action:', action)
            console.log('USER:', user)

        if (user == 'AnonymousUser'){//var user = {request.user} in navbar.html
            // console.log('User is not authenticated')
            addCookieItem(productId, action)//I add this when use guest visit that is not login
                    
        }else{
				 updateUserOrder(productId, action)
				 

            
        }
    })

})
   

  





function updateUserOrder(productId, action){
	console.log('User is authenticated, sending data...')

		var url = '/update_item/'

		fetch(url, {//create and use the fetch api to send a post request. to views
			method:'POST',
			headers:{
				'Content-Type':'application/json',
                'X-CSRFToken':csrftoken,//after you use getToken or getCookie include this =>cookie funation is in navbar.html

                /*Now, before we send this data we need to take care of creating and sending a csrftoken along with it otherwise
                Django wont let us send a post request without one. We'll cover this in the next step*/
               
                /*Because we are using Javascript to send data and are not actually submitting a form so we will 
                need to create our own token and pass it in with the post data. */
            }, 
           // In the post request we want to stringify and send our productId and action as a Json object. 
			body:JSON.stringify({'productId':productId, 'action':action})
		})
		.then((response) => {
		   return response.json();
		})
		.then((data) => {
		   location.reload()// This will alow us to see changes appear in our cart immediately once we render them.
		});
}


//guest cookie for non login user

function addCookieItem(productId, action){
	console.log('User is not authenticated')

	if (action == 'add'){
		if (cart[productId] == undefined){
		cart[productId] = {'quantity':1}
		

		}else{
			cart[productId]['quantity'] += 1
		}
	}

	if (action == 'remove'){
		cart[productId]['quantity'] -= 1

		if (cart[productId]['quantity'] <= 0){
			console.log('Item should be deleted')
			delete cart[productId];
		}
	}
	console.log('CART:', cart)
	document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
	
	location.reload()
}

