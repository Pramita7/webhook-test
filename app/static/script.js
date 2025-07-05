async function fetchEvents() {
  const res = await fetch('/events');
  const data = await res.json();
  const ul = document.getElementById('events');
  ul.innerHTML = '';
  data.forEach(ev => {
    const li = document.createElement('li');
    li.textContent = ev.message;
    ul.appendChild(li);
  });
}

fetchEvents();          // initial load
setInterval(fetchEvents, 15000);  // every 15 seconds
