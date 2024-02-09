const formModal = document.getElementById('form-modal')
console.log(formModal)

const cancelBtn = document.getElementById('cancel-btn')
const backdrop = document.getElementById('backdrop')

formModal.addEventListener('click', ((e)=> {
    console.log(e.target)
    if (e.target !== backdrop) return;
    formModal.classList.add('hidden')
}))

cancelBtn.addEventListener('click', ()=> { 
    formModal.classList.add('hidden')
})

$(document).ready(function(){

    $("#runButton").click(function() {
        var csrfToken = $("input[name=csrfmiddlewaretoken]").val();
        var dataId = $(this).data('id');

        $.ajax({
            url: '/descriptions/run/' + dataId,
            data: {
                csrfmiddelwaretoken: csrfToken,
                id: dataId
            }
            type: 'post',
            success: function(response) {
                
            }
        });

    });

});
