var uploader = {
  thumbnail: '',
  buttonName: '동영상 업로드',
  view: function ({ state }) {
    return m('div', [
    m('h1', 'Meokda'),
    m('div.thumb', { style: 'background-image:url(' + state.thumbnail + ')' }),
    m('input.file-input#file', {
      type: 'file',
      name: 'file',
      placeholder: '동영상 업로드',
      onchange: function (e) {
        let file = e.target.files[0];
        state.buttonName = e.target.value.split('\\').pop();
        let reader = new FileReader();
        reader.onload = function (e) {
          state.thumbnail = e.target.result;

          m.redraw();
        };
        reader.readAsDataURL(file);
      } }),

    m('label', { for: 'file' }, state.buttonName)]);


  } };


m.mount(document.getElementById("uploader"), uploader);