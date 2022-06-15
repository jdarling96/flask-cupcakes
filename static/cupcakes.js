URL = "http://127.0.0.1:5000/api/cupcakes"

const renderList = async() => {
    const res = await axios.get(URL)
    //console.log(res.data)

    for (let cupcakeData of res.data.cupcakes) {
        let newCupcake = $(displayResponse(cupcakeData));
        $('#list').append(newCupcake);
      }
    }
    



const displayResponse = (res) => {

    let { flavor, size, rating, image } = res
    return`
          <div class="row align-items-center">
          <img src="${image}" alt="${flavor}" class="img-thumbnail w-25 p-3">
          <h3>${flavor}</h3>
          <p>${size}</p>
          <p>${rating}</p>
          </div>
          `;
        
    }
    


$('#cupcake-form').on('submit', async function (evt) {
    evt.preventDefault()

    const newCupcakeResponse = await axios({url:URL, method:'POST', 
    data: {flavor: $('#flavor').val(), size: $('#size').val(), rating: $('#rating').val(), image: $('#image').val()}})

    let newCupcake = $(displayResponse(newCupcakeResponse.data.cupcake));
    $('#list').append(newCupcake);
    $('#cupcake-form').trigger('reset');
})


    renderList()







