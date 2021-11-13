//////////////////////////////////////////////////////////////
// GET GITHUB API
//////////////////////////////////////////////////////////////

var getGithubBtn = document.querySelector(".get-github-btn");

getGithubBtn.addEventListener("click", function() {
    console.log(this)
})

async function getCoderData() {
    var response = await fetch("https://api.github.com/users/adion81"); // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var coderData = await response.json();                              // We then need to convert the data into JSON format.
    return coderData;
}

var result = getCoderData();

console.log(result);