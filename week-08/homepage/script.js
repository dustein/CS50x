const modal_like = document.getElementById("janela-modal");
const botao = document.getElementById("liga-modal");
const fechar = document.getElementsByClassName("close-modal")[0];
const texto_modal = document.querySelector("#texto-modal");

const football_text = "Founded in 1902, Fluminense Football Club was the first Brazilian club to carry football in its name and has become one of the most popular in the country. A pioneer in sports, Fluminense FC spearheaded the creation of football leagues and tournaments, which influenced the formation of new teams and of the Brazilian National Team - the Seleção.  The historical Laranjeiras Stadium, inaugurated in 1919, was essential for making football popular in Brazil. In 1949, the International Olympic Committee recognized Fluminense FC as the most complete sports institution in the world, honoring the club with the Olympic Cup. The World Club Championship of 1952 and 5 national championships are among Fluminense FC’s most important conquers. As said by playwright Nelson Rodrigues, \"you can't walk around Fluminense without stumbling into glory\”.";
const music_text = "The Ramones were an American punk rock band formed in the New York City neighborhood Forest Hills, Queens in 1974. Known for helping establish the punk movement in the United States and elsewhere, the Ramones are often cited as the first true punk rock band. Although they never achieved significant commercial success, the band is seen today as highly influential in punk culture.";
const adventure_text = "Touring motorcycles are a class of motorcycle designed specifically for long-distance motorcycle trips. They generally feature large, powerful engines, cargo space or carriers for luggage, and an upright riding position.";
const ido_text= "Programming refers to a technological process for telling a computer which tasks to perform in order to solve problems. You can think of programming as a collaboration between humans and computers, in which humans create instructions for a computer to follow (code) in a language computers can understand.";

function close_button() {
  modal_like.style.display = "none";
}

function football_modal() {
  modal_like.style.display = "block";
  texto_modal.innerText = football_text;
}

function music_modal() {
  modal_like.style.display = "block";
  texto_modal.innerText = music_text;
}

function adventure_modal() {
  modal_like.style.display = "block";
  texto_modal.innerText = adventure_text;
}

function ido_modal() {
  modal_like.style.display = "block";
  texto_modal.innerText = ido_text;
}
