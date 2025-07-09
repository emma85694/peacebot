const TelegramBot = require('node-telegram-bot-api');
require('dotenv').config();

// Initialize Telegram bot with your token
const bot = new TelegramBot('7603920406:AAGVdKBCy0j9tPoIarYx-HZFMewLDDeC2_c', { polling: true });

console.log('🌻 Miss Peace Airdrop Bot Started...');

// Handle /start command
bot.onText(/\/start/, (msg) => {
  const chatId = msg.chat.id;
  
  bot.sendMessage(
    chatId,
    `🌻 <b>Welcome to the Miss Peace Airdrop!</b> 🌻\n\n` +
    `Complete these simple tasks to qualify:\n\n` +
    `1️⃣ JOIN OUR TELEGRAM CHANNEL:\n` +
    `👉 <a href="https://t.me/dawgs_on_sol">DAWGS on Sol</a>\n\n` +
    `2️⃣ JOIN OUR TELEGRAM GROUP:\n` +
    `👉 <a href="https://t.me/xtradeaig">XTrade AI Group</a>\n\n` +
    `3️⃣ FOLLOW OUR TWITTER:\n` +
    `👉 <a href="https://x.com/DAWGS_On_Sol">@DAWGS_On_Sol</a>\n\n` +
    `✨ After completing all tasks, click 👉 /submit to claim your 100 SOL reward!`,
    {
      parse_mode: 'HTML',
      disable_web_page_preview: true
    }
  );
});

// Handle /submit command
bot.onText(/\/submit/, (msg) => {
  const chatId = msg.chat.id;
  
  bot.sendMessage(
    chatId,
    `🪙 <b>STEP 4: Enter your Solana wallet address</b>\n\n` +
    `This is where we'll send your 100 SOL reward!\n\n` +
    `<i>Note: This is a test environment</i>`,
    {
      parse_mode: 'HTML',
      reply_markup: {
        force_reply: true
      }
    }
  );
});

// Handle wallet address submission
bot.on('message', (msg) => {
  if (!msg.text || !msg.reply_to_message) return;
  
  const chatId = msg.chat.id;
  const walletAddress = msg.text.trim();
  
  if (msg.reply_to_message.text.includes('STEP 4: Enter your Solana wallet address')) {
    if (/^[1-9A-HJ-NP-Za-km-z]{32,44}$/.test(walletAddress)) {
      bot.sendMessage(
        chatId,
        `🎉 <b>CONGRATULATIONS!</b> 🎉\n\n` +
        `You've successfully passed the Miss Peace Airdrop call!\n\n` +
        `💸 <b>100 SOL</b> is on its way to:\n` +
        `<code>${walletAddress}</code>\n\n` +
        `⏳ Estimated arrival: 5-10 minutes\n\n` +
        `✨ <i>"Well done, hope you didn't cheat the system!"</i>\n\n` +
        `⚠️ <b>Note:</b> This is a testing bot - no actual SOL will be sent.`,
        {
          parse_mode: 'HTML',
          disable_web_page_preview: true
        }
      );
    } else {
      bot.sendMessage(
        chatId,
        `❌ <b>Invalid Solana address!</b>\n` +
        `Please check and try again with /submit`,
        { parse_mode: 'HTML' }
      );
    }
  }
});

// Handle unknown commands
bot.onText(/\/(?!start|submit).+/, (msg) => {
  bot.sendMessage(msg.chat.id, `❌ Unknown command. Use /start to begin.`);
});
