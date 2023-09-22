const url = window.location.href


let quizBox = document.getElementById('quiz-box')

$.ajax({
    type: 'Get',
    url: `${url}data`,
    success: function(response){
        const data = response.data
        data.forEach(element => {
            const { question_text, answers, image } = element
            quizBox.innerHTML += `
                <div>
                    <b>${question_text}<b>
                </div>
                ${image ? `<img src="${image}" alt="Question Image" height="200" width="240">` : ''}
            `
            
            if (Array.isArray(answers)) {
                answers.forEach(answer => {
                    const { answer_text, image } = answer
                    quizBox.innerHTML += `
                    <div style="background-color: #f1f1f1; padding: 10px;">
                            <input type="radio" class="ans" name="${question_text}" id="${answer_text}-${answer_text}" value="${answer_text}"> 
                            <label for="${answer_text}-${answer_text}" style="vertical-align: top;">${answer_text}</label>
                            ${image ? `<label for="${answer_text}-${answer_text}"><img src="${image}" alt="Answer Image" height="200" width="240" ></label>` : ''}
                        </div>
                    `
                })
            }
        });
    },
    error: function(error){
        console.log(error)
    }
})
