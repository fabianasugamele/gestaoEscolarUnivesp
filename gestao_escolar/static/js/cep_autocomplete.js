document.addEventListener('DOMContentLoaded', function () {
    const cepInput = document.querySelector('[name="cep_residencia"]');
    const enderecoInput = document.querySelector('[name="endereco"]');
    const bairroInput = document.querySelector('[name="bairro"]');

    if (!cepInput) {
        console.error('Input de CEP não encontrado no DOM.');
        return;
    }

    cepInput.addEventListener('blur', function () {
        var cep = this.value.replace(/\D/g, '');

        if (!cep) {
            console.warn('CEP está vazio após formatação.');
            return;
        }

        var validacep = /^[0-9]{8}$/;

        if (!validacep.test(cep)) {
            alert("Formato de CEP inválido.");
            return;
        }

        fetch('https://viacep.com.br/ws/' + cep + '/json/')
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro na resposta da API: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                if (!data.erro) {
                    if (enderecoInput) enderecoInput.value = data.logradouro;
                    if (bairroInput) bairroInput.value = data.bairro;
                } else {
                    alert("CEP não encontrado.");
                }
            })
            .catch(error => console.error('Erro ao buscar o CEP:', error));
    });
});
