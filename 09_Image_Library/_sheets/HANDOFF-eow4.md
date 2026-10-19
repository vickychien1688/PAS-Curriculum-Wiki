# 交接任務：建 EOW4 手繪圖庫

專案在連接的資料夾 `/Users/chienhsiuting/Documents/GitHub/PAS Curriculum Wiki`。

## 先讀
- `09_Image_Library/style-bible.md`(畫風與命名規則)
- `09_Image_Library/_sheets/eow4-sheet-plan.md`(每張 sheet 的現成 prompt + 目標檔名)
- `09_Image_Library/vocab-image-list-eow4.md`(單字與狀態)

## 已完成
- EOW1 整庫;EOW2 由 Gemini 在跑;**EOW3 全部 113 字完成**(ChatGPT)。
- 這次做 **EOW4**:119 字 / 20 張 sheet(OBJECTS 1–7、ACTIONS 8–13、ADJ/ABSTRACT 14–18、PEOPLE 19、SETTINGS 20)。

## 工具
用 **ChatGPT**(Claude in Chrome 已連、ChatGPT 已登入)。EOW3 證實 ChatGPT 同一條對話連續生圖沒問題,**不需要每張開新對話**(那是 Gemini 的限制)。

## 每張流程(實測可行)
1. 第一則訊息先鎖畫風,再接 sheet 1 的圖。之後每張直接貼 `eow4-sheet-plan.md` 裡那張的 prompt(開頭就是 `Another image:`),用主輸入框送出。
   - 鎖畫風開場白範例:「I'm building a consistent picture-book icon set for a children's worksheet, ages 6 to 8. Apply this same style to EVERY image in this chat: cute hand-drawn children's storybook illustration, soft warm watercolour and colored-pencil style (NOT flat vector, NOT a hard sticker icon), rounded chunky shapes, soft hand-drawn outline, gentle shading, pure white background, no text/letters/numbers anywhere.」+ 該 sheet 的 grid 描述。
2. 等生圖完成(約 40–90 秒;用 `img.naturalWidth>=700` 抓最後一張判斷完成)。
3. **下載**:在頁面跑 JS,fetch 該圖 blob → `<a download="eow4-sheetNN.png">` 觸發下載。
   - 程式下載免手勢即可,檔案會落在 Chrome 下載資料夾 **`/Users/chienhsiuting/Documents/Claude/Projects/rpg disgen/character_images/_inbox`**(要先把這個資料夾接上來才讀得到)。
4. **裁切**:用 `09_Image_Library/_sheets/crop_grid.py`(已留好)。
   - 用法:`python3 crop_grid.py <輸入png> <rows> <cols> <輸出資料夾> "word1,word2,..."`(row-major;空格填 `skip`)。
   - 它會偵測留白切格、各格貼齊置中成正方形、輸出 300px。
5. **存檔**:每字 `words/<word>/<word>-v1-color.png`,並把 color 轉灰階存 `-v1-bw.png`(`Image.open(...).convert("L")`);寫 `words/<word>/prompt.txt`。
6. 在 `vocab-image-list-eow4.md` 把該字標 `DONE`。
7. 捨棄任何填充字。每完成一級(category)給 Vicky 看一張 contact sheet。

## 注意
- 裁切完用小張 contact sheet 確認「圖的內容對得上檔名」(ChatGPT 偶爾會調整格內順序)。
- 物件/食物會偏亮一點、人物偏柔和水彩;整體仍是同一套童書風。
- 少數建築招牌/標籤可能有極小字樣,worksheet 尺寸下看不出來;若要零文字就重跑該張。
- 分批跑、隨時回報。
