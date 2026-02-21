const express = require("express");

const app = express();
const PORT = 5000;

app.use(express.json());


app.get("/", (req, res) => {
  res.send("🚀 Branding Automation System Backend Running");
});


app.get("/generate-brand", (req, res) => {
  const businessType = req.query.businessType;

  if (!businessType) {
    return res.send("Please provide businessType in URL like ?businessType=Tech");
  }

  const brandNames = [
    `${businessType}Hub`,
    `${businessType}ify`,
    `Next${businessType}`,
    `${businessType}Sphere`,
    `Smart${businessType}`
  ];

  res.json({
    success: true,
    brandSuggestions: brandNames
  });
});


app.get("/generate-slogan", (req, res) => {
  const brandName = req.query.brandName;

  if (!brandName) {
    return res.send("Please provide brandName in URL like ?brandName=TechHub");
  }

  const slogans = [
    `${brandName} - Empowering Your Future`,
    `${brandName} - Innovation Meets Style`,
    `${brandName} - Where Ideas Become Reality`,
    `${brandName} - Redefining Excellence`,
    `${brandName} - Built for Success`
  ];

  const slogan = slogans[Math.floor(Math.random() * slogans.length)];

  res.json({
    success: true,
    slogan: slogan
  });
});


app.get("/generate-caption", (req, res) => {
  const brandName = req.query.brandName;

  if (!brandName) {
    return res.send("Please provide brandName in URL like ?brandName=TechHub");
  }

  const captions = [
    `🌟 Welcome to ${brandName}! Transforming ideas into reality. #Innovation #Branding`,
    `🚀 Discover ${brandName} - Where creativity meets excellence! #Startup #Brand`,
    `🔥 ${brandName} is here to revolutionize your business journey! #Branding #Growth`
  ];

  const caption = captions[Math.floor(Math.random() * captions.length)];

  res.json({
    success: true,
    caption: caption
  });
});


app.listen(PORT, () => {
  console.log(`✅ Server running on http://localhost:${PORT}`);
});