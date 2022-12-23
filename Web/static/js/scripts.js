$(document).ready(function(){
	var form = $('#price_and_form');
	console.log(form);
	/*var shoping_cart_btn = $('#')*/
	form.on('submit', function(btn_submitted){
		btn_submitted.preventDefault();
		console.log('Submitted');
		var nmb = $('#count1').val()
		console.log("count:",nmb);
		var submit_btn =  $('#btn_self_page');
		var product_id = submit_btn.data("product_id");
		var product_name = submit_btn.data("product_name");
		var product_discount = submit_btn.data("product_discount")
		var product_price_with_discount = submit_btn.data("product_price_with_discount")
		var product_price = submit_btn.data("product_price")
		if (product_discount > 0) {
			console.log("discount price:", product_price_with_discount)
			console.log("discount %", product_discount)
		}
		console.log("id:",product_id);
		console.log("Name:",product_name);
		console.log("price:",product_price);

			var data = {};
			data.product_id = product_id;
			data.product_price = product_price;
			data.product_name = product_name;
			data.product_discount = product_discount;
			data.product_price_with_discount =product_price_with_discount;
			data.nmb = nmb;
			var csrf_token = $('#price_and_form [name = "csrfmiddlewaretoken"]').val();
			data["csrfmiddlewaretoken"] = csrf_token;
			
			var url = form.attr("action");
			console.log(data)
			$.ajax({
			    url: url,
				type: 'POST',
				data: data,
				cache: true,
				success: function (data) {
					console.log("OK");
					console.log(data.product_total_number);
					if (data.product_total_number) {
						$('#basket_total').text(data.product_total_number);	
					}
					

				}
				/*error: function() {console.log("ERROR")}*/
			})

		$('.basket-items ul').append('<li>'+product_name + ' ' + product_price +'$ ' + nmb +'шт.' + '<a class="remove-product" href="/" style="text-decoration: none;">x</a>' + '</li>');
	});
/*-----------------------------------------------------------------------------*/
	$('.basket-container').mouseout(function(){
		$('.basket-items').addClass('hidden');
	})
	$('.basket-container').mouseover(function(){
		$('.basket-items').removeClass('hidden');
	})
	$(document).on('click', '.remove-product',function(e){
		e.preventDefault();
		$(this).closest('li').remove();
	})
/*-----------------------------------------------------------------------------*/
	$(document).on('click', '.btn-succes',function(evnt){
		evnt.preventDefault();
		var product_id = $(this).data("product_id");
		var product_name = $(this).data("product_name");
		var product_discount = $(this).data("product_discount");
		var product_price_with_discount = $(this).data("product_price_with_discount");
		var product_price = $(this).data("product_price");
		if (product_discount > 0) {
			console.log("discount price:", product_price_with_discount);
			console.log("discount %", product_discount);
			}
		console.log("id:",product_id);
		console.log("Name:",product_name);
		console.log("price:",product_price);
		$('.basket-items ul').append('<li>'+product_name + ' ' + product_price +'$ '+'шт.' + '<a class="remove-product" href="/" style="text-decoration: none;">x</a>' + '</li>');
	})


})





