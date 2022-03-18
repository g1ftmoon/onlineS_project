let pass_inp = document.getElementById('pass-inp');
let show_pass_btn = document.getElementById('login-pass-icon');
show_pass_btn.addEventListener('click', () => {
    if(pass_inp.attributes.type.value === 'password'){
        pass_inp.attributes.type.value = 'text'
    }else{
        pass_inp.attributes.type.value = 'password'
    }
});