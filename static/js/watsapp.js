            let radioList = document.querySelectorAll('input');
            let underLine = document.querySelector('.underline');
            let content = document.querySelector('.content');

            function setIndex() {
                const i = this.style.getPropertyValue('--i');
                underLine.style.setProperty('--i', i);
                content.style.setProperty('--i', i);
            }

            radioList.forEach((item) =>
                item.addEventListener('click', setIndex))

            let back = document.querySelector('.back');
            let chatBox = document.querySelector('.chatBox');
            let open = document.querySelector('.open');

            back.onclick = function() {
                chatBox.classList.add('hide');
            }

            open.onclick = function() {
                chatBox.classList.remove('hide');
            }
