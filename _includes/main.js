{%- assign upgrade_data_file = page.upgrade_data_file -%}
{%- assign data = site.data[upgrade_data_file] -%}
{%- assign tbd = data.activation_epoch | downcase -%}




{%- if tbd != "tbd" -%}
const epochTime = Date.now();
const activationTime = {{data.activation_unix_epoch}} * 1000;
const timer = document.getElementById("timer");
const localTime = document.getElementById("local-time");

// show poap section if activation time passed
if (activationTime < epochTime) {
  try {
    document.getElementById("poap").style.display = "block";
  } catch {
    // required to prevent error if poap section disable
  }
}


const formatTime = (t) => {
  const days = Math.floor(t / (1000 * 60 * 60 * 24));
  const hours = Math.floor((t % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  const minutes = Math.floor((t % (1000 * 60 * 60)) / (1000 * 60));
  const seconds = Math.floor((t % (1000 * 60)) / 1000);
  return `${days}d ${hours}h ${minutes}m ${seconds}s`;
};

const updateCountdown = () => {
  const now = Date.now();
  const distance = activationTime - now;

  if (distance <= 0) {
    timer.textContent = "✅ Activated";
    timer.classList.add("activated");
    clearInterval(interval);
  } else {
    timer.textContent = formatTime(distance);
  }

  // show poap section if within an hour of activation
  if ((distance) < 3600000) {
    document.getElementById("poap").style.display = "block";
  }
};

const date = new Date(activationTime);
localTime.textContent = date.toLocaleString();

updateCountdown();
const interval = setInterval(updateCountdown, 1000);
{%- endif -%}




