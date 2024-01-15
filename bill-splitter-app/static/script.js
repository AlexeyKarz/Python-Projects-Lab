function addFlatmate() {
    const flatmatesDiv = document.getElementById("flatmates");
    const newId = `flatmate-${flatmatesDiv.children.length}`;
    const flatmateDiv = document.createElement("div");
    flatmateDiv.id = newId;

    flatmateDiv.innerHTML = `
        <label for="name-${newId}">Name:</label>
        <input type="text" id="name-${newId}" name="name-${newId}">
        
        <label for="days-${newId}">Days in House:</label>
        <input type="text" id="days-${newId}" name="days-${newId}">

        <button class="remove" type="button" onclick="removeFlatmate('${newId}')">Remove</button>
    `;

    flatmatesDiv.appendChild(flatmateDiv);
}

window.onload = function() {
    addFlatmate();
};


function removeFlatmate(id) {
    const flatmateDiv = document.getElementById(id);
    flatmateDiv.parentNode.removeChild(flatmateDiv);
}

let globalFormData;

function submitForm() {
    const billAmount = document.getElementById("amount").value;
    const billPeriod = document.getElementById("period").value;

    const flatmatesData = Array.from(document.getElementById("flatmates").children).map(flatmateDiv => {
        return {
            name: flatmateDiv.querySelector("input[type='text'][name^='name-']").value,
            daysInHouse: flatmateDiv.querySelector("input[type='text'][name^='days-']").value
        };
    });

    globalFormData = {
        amount: billAmount,
        period: billPeriod,
        flatmates: flatmatesData
    };

        fetch('/results', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(globalFormData)
    })
    .then(response => response.json())
    .then(data => {
        displayResults(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

function displayResults(data) {
    // Display the data on the screen
    // For example, append the results to an element in your HTML
    const resultsDiv = document.getElementById("results");
    resultsDiv.innerHTML = ''; // Clear previous results
    Object.keys(data).forEach(key => {
        resultsDiv.innerHTML += `<p>${key} owes: $${data[key].toFixed(2)}</p>`;
    });

    // Add a button for downloading the PDF
    const downloadBtn = document.createElement("button");
    downloadBtn.innerText = "Download PDF";
    downloadBtn.onclick = () => downloadPDF();
    resultsDiv.appendChild(downloadBtn);
}

function downloadPDF() {
    // Use globalFormData in the fetch request to '/download_pdf'
    fetch('/download_pdf', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(globalFormData)  // Use the global variable here
    })
    .then(response => response.blob())
    .then(blob => {
        // Create a Blob from the PDF Stream
        const file = new Blob([blob], { type: 'application/pdf' });
        const fileURL = URL.createObjectURL(file);

        // Create a link for download
        const fileLink = document.createElement('a');
        fileLink.href = fileURL;
        fileLink.setAttribute('download', 'flatmates_bill.pdf');
        document.body.appendChild(fileLink);

        fileLink.click();
    })
    .catch(error => {
        console.error('Error:', error);
    });
}