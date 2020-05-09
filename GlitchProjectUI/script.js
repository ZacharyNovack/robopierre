// TEXT CONSTANTS
var who_am_i = "My name is Current Event Recaller with Vague And aNnoying Tendency to Elevate Spanish flu, but you can call me CERVANTES. " +
    "My dads like to call me RoboPierre but they couldn't think of a good acronym to fit that."+
    "<p>My job is to deliver to you yesterday's news of today."+
    " This so-called history of the future is comprised of news articles, stories, poetry, et cetera, all of which is relevant to the "+
    "current situation you find yourself in, but was written about a hundred years ago or more."+
    " Also, due to some bugs and quirks in my virtual flux capacitor, pretty much everything I give you will be in the french language."+
    " I am very sorry! My creators are still trying to figure out why I do this.<p>If you want to learn more, type <b>about_project</b>."

var audio_files = {

  "0":{

    "text" : "<strong>La Grippe a' la Chambre</strong><p>Apres l\'Academie de sciences, l\'Academie de medecine, la Chambre s\'est occupee, hier, de la grippe.<p>Depuis longtemps, la Chambre est moins une assemblee de deliberante qu\'une academie d\'aucuns dissent meme un conseil general. En effet, elle emet sure tout des voeux et les discussions auxquelles donnent lieu les questions sure lesquelles elle exprime ces voeux au gouvernment, son, au propre du mot, des discours academiques, puisque le gouvernement ne leur donne que la suire qui lui plait.<p>Naturellement, les medecins et les pharmaciens prirent part au debat sur la grippe. Mais je remarque que les chose les plus sensees et les explications les plus lucides sure la propagation du fleau, furent dites surtout par des profanes.<p>Ainsi, MM. Dumont et Merlin, interpellateurs, disserterent fort congrument sur &lt&ltl\'etiologie du fleau&gt&gt. Poncet, qui commenca par declarer qu'il n\'etait &lt&lt ni medecin, ni pharmacien, ni malade &gt&gt, montra, par un exemple concret, comment la grippe se propage.<p>-L\'Humanite-19181026",

    "audio":["https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLaGrippe3.mp3?v=1588837482362",

             "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLaGrippe2.mp3?v=1588837482364",

            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLaGrippe1.mp3?v=1588837482427",
            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLaG2.mp3?v=1589038084466",
            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLaG1.mp3?v=1589038086319"]

  },

  "1":{

    "text":"<strong>EN QUARANTAINE!</strong><p>Bilbao, 1er janvier. - La police fait subir un interrogatoire a tous les sujets russes appartenant aux equipages des navires etrangers qui debarquent a Bilbao. Ceux d'entre eux qui sont suspects de bolchevisme sont immediantement arretes et reembarques, avec defense absolue de descendre a terre. Une dizaine d'arrestations ont ete operees dans ces conditions.<p>-L\'Humanite-19190101",

    "audio":["https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FEnQuarantine2.mp3?v=1588837551945",

            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FEnQuarantine3.mp3?v=1588837551974",

            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FEnQuarantine1.mp3?v=1588837552024"]

  },

"2":{

    "text":"<strong>POUR LUTTER CONTRE LA GRIPPE</strong><p>L'adminitration avait pense a utiliser les asiles de vieillards du departement de la Seine pour hospitaliser "+
"les personnes atteintes de la grippe.<p>Le troisieme commission du conseil general ne s'est pas inclinee " +
"et a oppose un refus en faisant remarquer qu'il suffirait de rendre a l'Assistance publique l'asile de la "+
"Maison-Blanche, toujours occupe par l'autorite militaire.<p>D'autre part. on pourrait egalement utiliser " +
"une maison religieuse de la rue de Vaugirard qui contient deux cents lits.<p>-L'Humanite-19181002",

    "audio":["https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FPL1.mp3?v=1589038084804"]

  },

"3":{

     "text":"<b>L'INTERNATIONALE</b><p>Un journal du matin a publie un &lt&lt radio sensationnel &gt&gt qui aurait ete lance par le gouvernment " +
"bolchevik de Moscou.<p>Ce radio contient une protestation contre la reunion de L'Internationale qui doit avoir lieu a Lausanne.<p>"+
"S'agit-il la d'un document authentique? Il convient d'attendre pour repondre a cette question.<p>" +
"En yout cas, meme si, dans l'ardeur de la bataille terrible qu'ils livrent depuis un an et demi, les bolcheviks s'etaient laisse "+
"entrainer a lancer l'anatheme contre l'Internationale telle qu'elle serait composee a Lausanne, "+
"ce ne serait la qu'un incident de la grande lutte sociale qui ebranle le monde entier. "+
"Aussi nous sera-t-il permis de sourire en entendant le dithyrambe d'allegresse par lequel le "+
"<i>Temps</i> accueille cette publication. &lt&lt L'Internationale est morte, dit-il, le socialisme est use, brise, etc. &gt&gt<p>-L'Humanite-19190103",

    "audio":["https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLI1.mp3?v=1589038084541",
            "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2FLI2.mp3?v=1589038085745"]

  }

}

var about_text = "Website designed by Joseph Sandler and Zachary Novack."+
    " Sound synthesis by Zachary Novack with assistance from Joseph Sandler and Gabriel Garcia. Voices used: Joseph Sandler, Jocelyn Dueck" +
    "<p>Current event sounds generated by vocoding spoken text to digital instruments and synthesizers using Ableton Live and Arturia Pigments. The midi music used to "+
    "do this was generated using Google Magenta's Polyphony RNN on a corpus of piano works by Debussy, Ravel, and Chopin. Type <b>github</b> to be taken to the external github repo for this project or <b>soundcloud</b> to be taken to a Soundcloud profile with all of the vocoded tracks.."+
    "<p>Interested in contributing your voice to this project? Type <b>contribute</b> for more information on submitting speech recordings for CERVANTES." +
    "<p>Project under Creative Commons Attribution NonCommercial ShareAlike license. For more information type <b>license</b>. (All of these commands will take you to an external page)."
//
//

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

function pick_newsstory() {
  var n = Object.keys(audio_files).length;
  var i = getRandomInt(n).toString();
  var j = getRandomInt(audio_files[i].audio.length);
  var res = {text:audio_files[i].text,
            audio:audio_files[i].audio[j]}
  return res;
}

function do_console_command(input) {
  var sound = document.getElementById("robot-sound");
  var audio_src = "";
  var output_text="";
  var changeAudio = true;  
  switch(input) {
      case("about_project"):
        changeAudio = false;
        output_text = about_text;
        break;
      case("help"):
        //audio_src = "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2Fhelp.mp3?v=1587183970199";
        changeAudio = false;  
      output_text = "Hello! I am here to help. I still have much to learn, but here are some things you can do:<p><table id=\"help-table\" style=\"border:0;\"><tr><td><b>about_cervantes</b></td><td>Learn about me and why I am here!</td></tr>"+
          "<tr><td><b>about_project</b></td><td>Learn about why I was made and how you can help me grow even more!</td></tr>" +
          "<tr><td><b>get_current_events</b></td><td>Let me tell you the news! Or perhaps some poetry if you're lucky. I will sing it to you in one of my special voices.<br>Because of how I was made, it will be in french, and probably from a newspaper 100 years old or so. But I promise it's relevant to your life today!If you ask <b>multiple times<b>, you might get a diffrent song! Or perhaps the same song! Or maybe the same words. Who knows!.</td></tr>"+
          "<tr><td><b>++</b></td><td>For volume up</td></tr><tr><td><b>--</b></td><td>For down</td></tr>" + 
          "<tr><td><b>shut_up</b></td><td>Make me stop talking (how rude...)</td></tr>"+
          "<tr><td><b>license</b></td><td>This will redirect you to another page about my licensing information. Licensed under Creative Commons Attribution NonCommercial ShareAlike.</td></tr>" +
          "<tr><td><b>contribute</b></td><td>This will redirect you to another page where you can learn about how you can give me your voice so that I can grow and learn more!</td></tr>" +
          "<tr><td><b>play_promo</b></td><td>This will redirect you to another page where you can watch my promotional video</td></tr>"
          "</table><p>If you still aren't sure what to do, or I seem broken, go to <b>about_project</b> and let one of my dads know I'm broken.";
        break;
      case("hello"):
        output_text =  "Hi! How are you?";
        break;
      case("about_cervantes"):
        audio_src = "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2Fwho_are_you.mp3?v=1587183066363"
        output_text = who_am_i;
        break;
      case("_jesse_"):
      case("./jesse.out"):
        output_text = "./jesse.out -BADMEMES -supresswarnings<br>You must be Jesse. My creators told me about you. They said you like Satie. This is logical because your names rhyme. They also said this was what you call a \"bad meme\".";
        audio_src = "https://cdn.glitch.com/32d49bb5-00eb-4105-853e-80c89fd9f764%2Fjesse.mp3?v=1587186227501";
        break;
      case("shut_up"):
        output_text = "Shutting up...";
      changeAudio = false;
        sound.pause();
        break;
      case("get_current_events"):
        var curr_event_obj = pick_newsstory();
        output_text = "current_events.out -recall 1918_19 -langue pas_anglais<p>Getting a news story relevant to today...<p>" + curr_event_obj.text;
        audio_src = curr_event_obj.audio;
        break;
      case("++"):
        if (sound.volume < 0.9){ sound.volume += .1;
        output_text = "INCREASING dB";}
        else {
          output_text = "ERROR: ALREADY AT MAXIMUM VOLUME";
        }
        changeAudio = false;
        break;
      case("--"):
        if (sound.volume > 0.1) {sound.volume -= .1;
                              output_text = "DECREASING dB"}
        else {
              output_text="ERROR: ALREADY AT MINIMUM VOLUME";
        }
        changeAudio = false;
        break;
      case("license"):
        window.location.href ="https://creativecommons.org/licenses/by-nc-sa/4.0/";
        break;
      case("contribute"):
        window.location.href="https://forms.gle/M4KJ4cv6tQjzt3kc8";
        break;
      case("play_promo"):
        window.location.href="https://youtu.be/Crx-WI6c8h8";
        // sound.pause();
        // var video = document.getElementById("promoVideo");
        // $("#console").attr("visibility", "hidden");
        // $(video).attr("visibility", "visible");
        // video.play();
        // changeAudio=false;
        break;
      case("github"):
        window.location.href ="https://github.com/ZacharyNovack/robopierre";
        break;
      case("soundcloud"):
        window.location.href= "https://soundcloud.com/robopierre";
        break;
    default:
      output_text = "I am sorry. I do not know what you are asking me.<br>UNKNOWN COMMAND: " + input;
      changeAudio = false;
      break;
  }
  if (changeAudio){
  sound.setAttribute("src", audio_src);
  sound.play();}
  return output_text;
}