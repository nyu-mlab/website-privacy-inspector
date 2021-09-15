const { collector } = require("./build");
const { join } = require("path");
const fs = require('fs');
(async () => {
  const EMULATE_DEVICE = "";

  // Save the results to a folder
  let OUT_DIR = true;

  // The URL to test
  const URL = process.argv[2];
  var log = process.argv[3];
  console.log(log);

  var url_list = URL.split(",");
  //const url1 = string[0];
  //const url2 = string[1];
  var today = new Date();
  var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
  var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
  var dateTime = date+' '+time;
  log = log + dateTime  + " Decoding of encoded URL started \n";

  for(let i =0;i<url_list.length;i++)
{
    date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    dateTime = date+ " " +time;
    var url_base64 = url_list[i];
    var buff = Buffer.from(url_base64, 'base64');
    var url = buff.toString('ascii');
    date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
    time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
    dateTime = date+ " " +time;
    log = log + dateTime + " " + url_base64 + " decoded to " + url + "\n";
    var defaultConfig = {
    inUrl: url, //remove https
    numPages: 0,
    headless: true,
    emulateDevice: EMULATE_DEVICE,
  };
    fs.writeFileSync('logfile.txt',log);
    var destination_dict = url_list[i]
        var result = await collector(
    OUT_DIR
      ? { ...defaultConfig, ...{ outDir: join(__dirname, destination_dict) } }
      : defaultConfig
  );
  if (OUT_DIR) {
    console.log(
      `For captured data please look in ${join(__dirname, destination_dict)}`
    );
  }
}
