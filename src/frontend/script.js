let urlString = window.location.href;
let hostName = window.location.hostname;
let url = new URL(urlString);

// Determine the WebSocket URL based on the current protocol (http or https)
let wsProtocol = url.protocol === 'https:' ? 'wss:' : 'ws:';

// Construct the WebSocket URL using the host from the current URL
const wsUrl = `${wsProtocol}//${hostName}/ws`;
// const wsUrl = `ws://localhost:8000/ws`
// Make a websocket connection
let ws = new WebSocket(wsUrl);

document.addEventListener('DOMContentLoaded', () => {
    let table = document.querySelector("#process-table");
    let dataTable = new DataTable(table);
});


function addRow(row) {
    $('#process-table').DataTable().row.add([row.process_id, row.file_name, row.file_path,
    row.description, row.start_time, row.end_time,
    row.time_taken, (row.percentage).toFixed(2)]).draw(false);
}

const addRow = (row) => {
    dataTable.row.add(
        [row.process_id, row.file_name, row.file_path,
        row.description, row.start_time, row.end_time,
        row.time_taken, (row.percentage).toFixed(2)
    ])
}
// On receiving a message, append it to the unordered list `messages`
const processMessage = (event) => {
    console.log('Received Data');
    dataTable.clear().draw();
    let data = JSON.parse(event.data);
    data.forEach((item, index) => {
        addRow(item);
    })
}

// Bind processMessage method defined above to the
ws.onmessage = processMessage;
