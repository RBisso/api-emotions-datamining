const result = {
  input : "estou morrendo de medo",
  emotion : "medo"
}

const resultDiv = document.getElementById("result");


const btn = document.getElementById("submit");
btn.addEventListener("click", submitHandler);

function submitHandler (e){
  e.preventDefault();
  reponseData = {}
  textToClassify = {text: document.getElementById('text').value}
  fetch('api/', {
    method:'POST',
    headers:{
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(textToClassify),
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    const template = `
      <div class="result-input">${data.text}</div>
      <div class="result-emotion">${data.class}</div>
    `
    resultDiv.innerHTML = template;
  })
  .catch((error)=> {
      console.error('Error:', error);
  })   
  /*
  const template = `
  <div class="result-input">${responseData.text}</div>
  <div class="result-emotion">${responseData.class}</div>
`
  resultDiv.innerHTML = template;
  */
}