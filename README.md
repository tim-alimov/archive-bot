# Telegram Archive Bot

A lightweight, self-hosted Telegram bot that transforms a standard Telegram storage channel into an organized, searchable digital library. Instead of forcing users to scroll through a chaotic channel feed, this bot provides a clean menu interface and direct shareable links to your files, videos, and documents.

---

## Features

- **In-Channel Indexing:** Label, name, and assign categories to files directly inside your archive channel using inline buttons.
- **Clean Menu UI:** End-users browse resources using simple Reply Keyboards and inline buttons without channel chatter.
- **Deep Linking Support:** Share direct links (`t.me/YourBot?start=item_id` or `t.me/YourBot?start=cat_id`) in video descriptions or social posts to send users straight to a specific file or category.
- **Minimal Self-Hosting:** Runs everywhere with zero complex setup—just set your `.env` variables and start the bot.
- **Admin Security:** Restricted management rights ensure only the specified admin can add, edit, or categorize files.

---

## Architecture & Database

The actual file storage is offloaded to Telegram's infrastructure via your archive channel. Consequently, the local database only handles lightweight metadata mapping (e.g., mapping category IDs, item names, and Telegram message IDs).

* **SQLite by Default:** SQLite is intentionally used for maximum simplicity, zero configuration, and easy self-hosting out of the box.
* **ORM Flexibility:** Built with **SQLAlchemy**, allowing you to seamlessly transition to PostgreSQL, MySQL, or another SQL database whenever scale or infrastructure requirements demand it.

---

## Quick Start

### 1. Prerequisites

- Python 3.10+ (or Docker)
- A Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- A private Telegram Channel to act as your archive storage

### 2. Environment Setup

Clone the repository and create a `.env` file in the root directory:

```bash
git clone [https://github.com/your-username/telegram-archive-bot.git](https://github.com/your-username/archive-bot.git)
cd telegram-archive-bot
cp .env.example .env
