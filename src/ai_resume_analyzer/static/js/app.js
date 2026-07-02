async function copySection(id, button) {

    const element = document.getElementById(id);

    if (!element) {
        return;
    }

    const text = element.innerText.trim();

    try {

        if (navigator.clipboard) {

            await navigator.clipboard.writeText(text);

        } else {

            const textarea = document.createElement("textarea");

            textarea.value = text;

            textarea.setAttribute("readonly", "");

            textarea.style.position = "absolute";

            textarea.style.left = "-9999px";

            document.body.appendChild(textarea);

            textarea.select();

            textarea.setSelectionRange(0, 999999);

            const successful = document.execCommand("copy");

            document.body.removeChild(textarea);

            if (!successful) {
                throw new Error("Copy failed");
            }

        }

        showCopied(button);

    } catch (err) {

        console.error(err);

        alert("Unable to copy. Please press Ctrl+C.");

    }

}

function showCopied(button) {

    const icon = button.querySelector("i");

    const text = button.querySelector("span");

    button.classList.add("copied");

    icon.className = "fa-solid fa-check";

    text.textContent = "Copied";

    setTimeout(() => {

        button.classList.remove("copied");

        icon.className = "fa-regular fa-copy";

        text.textContent = "Copy";

    }, 1800);

}

async function copyValue(value, button){

    if(!value) return;

    await navigator.clipboard.writeText(value);

    button.classList.add("copied");

    button.innerHTML='<i class="fa-solid fa-check"></i><span>Copied</span>';

    setTimeout(()=>{

        button.classList.remove("copied");

        button.innerHTML='<i class="fa-regular fa-copy"></i><span>Copy</span>';

    },1500);

}