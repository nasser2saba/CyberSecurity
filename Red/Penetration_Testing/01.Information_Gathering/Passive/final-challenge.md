# Into - Discovering the network 

You are hired to do a recognition test (and only passive recognition) for the company adlp-corp.com.

- https://adlp-corp.com/

Using all the techniques you learn to gather information, try to know your target as well as possible.

You have to find 9 flags that prove your passage. Be careful, not all flags have the same syntax.


You must write a mini report on how you found the flags. 

**Validation link**
https://forms.gle/rSYHeGWr4imk7oyS9



# THe Process

I started up by going to chatgpt ~ I got the following answer: 

To perform a passive recognition test on the website adlp-corp.com and find the 9 flags, you should follow these steps:

1. **Explore the Website:**
   - Visit the main page of the website: [adlp-corp.com](https://adlp-corp.com/).
   - Navigate through different sections such as Home, About Us, Services, Contact Us, etc.
   - Look for any subdomains or additional pages linked from the main page.

2. **View Source Code:**
   - Right-click on different pages of the website and select "View Page Source."
   - Look through the HTML code for any comments or hidden elements that might contain flags.

3. **Inspect Elements:**
   - Use browser developer tools (F12) to inspect elements on the pages. Check for any hidden elements or metadata.

4. **Check Robots.txt:**
   - Visit `https://adlp-corp.com/robots.txt` to see if there are any disallowed directories or files that could contain flags.

5. **Look for Hidden Directories and Files:**
   - Manually try to access common hidden directories or files, such as `https://adlp-corp.com/.htaccess`, `https://adlp-corp.com/.git`, etc.

6. **Check for Sitemap:**
   - Visit `https://adlp-corp.com/sitemap.xml` or `https://adlp-corp.com/sitemap_index.xml` to find all available pages on the website.

7. **Google Dorking:**
   - Use specific search queries on Google to find information related to the site. For example, `site:adlp-corp.com` can help you find indexed pages.

8. **Look for Online Tools:**
   - Use online tools like [Shodan](https://www.shodan.io/) or [Censys](https://censys.io/) to gather additional information about the website.

9. **Review Social Media and Other External Sources:**
   - Check if the company has social media profiles or any presence on forums or other websites. These might contain hints or direct links to flags.

Now, let's start with the initial steps:

### Step 1: Explore the Website
Visit [adlp-corp.com](https://adlp-corp.com/) and start exploring the main page and its sections.

### Step 2: View Source Code
- Go to the main page.
- Right-click and select "View Page Source."
- Look through the HTML code for comments or hidden elements.

### Step 3: Inspect Elements
- Use the browser's developer tools to inspect elements and look for any hidden elements or metadata.

### Step 4: Check Robots.txt
- Visit `https://adlp-corp.com/robots.txt` in your browser.

### Step 5: Look for Sitemap
- Visit `https://adlp-corp.com/sitemap.xml` or `https://adlp-corp.com/sitemap_index.xml`.

By following these steps, you should be able to gather information and potentially find the 9 flags required for your exercise. If you encounter any specific issues or need further assistance with any step, let me know!


First thing I did was jump to Step 4 and 5, I checked the links and found my first flag; 
> ADLP{ROBOTS_TXT_G569816}

Then I went to https://adlp-corp.com/sitemap.xml and got the following; 
This XML file does not appear to have any style information associated with it. The document tree is shown below.
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
<url>
<loc>ADLP{SITM4PAS_XML_G569816}</loc>
<lastmod>2018-06-04</lastmod>
</url>
</urlset>
Another flag found: 
> ADLP{SITM4PAS_XML_G569816}

Then https://adlp-corp.com/sitemap_index.xml
But nothing was actually found on that page

2 Flags were found for now, it was mentioned that there was a hidden pdf file that had a flag. 
So I went back to Chatgpt and tried to figure out how to access that hidden pdf file.

Remember the previous page I was on with the ADLP{SITM4PAS_XML_G569816} flag, there was a link mentioned http://www.sitemaps.org/schemas/sitemap/0.9
I went on it and found a mini tree, welp, nothing in the whole tree of sitemap

then I used gobuster, to Brute Force the website 
command used: `gobuster dir -u https://adlp-corp.com -w /home/SabaNasser/SecLists/Discovery/Web-Content/common.txt -x pdf`

And got the folliwng in return: 

Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     https://adlp-corp.com
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /home/SabaNasser/SecLists/Discovery/Web-Content/common.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              pdf
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta.pdf             (Status: 403) [Size: 279]
/.htaccess            (Status: 403) [Size: 279]
/.hta                 (Status: 403) [Size: 279]
/.htpasswd            (Status: 403) [Size: 279]
/.htpasswd.pdf        (Status: 403) [Size: 279]
/.htaccess.pdf        (Status: 403) [Size: 279]
/css                  (Status: 301) [Size: 314] [--> https://adlp-corp.com/css/]
/font                 (Status: 301) [Size: 315] [--> https://adlp-corp.com/font/]
/images               (Status: 301) [Size: 317] [--> https://adlp-corp.com/images/]
/index.html           (Status: 200) [Size: 26335]
/js                   (Status: 301) [Size: 313] [--> https://adlp-corp.com/js/]
/robots.txt           (Status: 200) [Size: 24]
/server-status        (Status: 403) [Size: 279]
/sitemap.xml          (Status: 200) [Size: 202]
Progress: 9460 / 9460 (100.00%)
===============================================================
Finished
===============================================================

So I started searching again.
Starting with the first link https://adlp-corp.com/css/ I ended up with the same tree, but from the "root" let's say.
The more I dug the more I ended up in pages with a ton of characters, which I'm not going to go through.
Navigating through the tree, I didn't find anything, and just as I clicked on the last link, I ended up finding this flag: 
> ADLP{CSS_HSBUSGYIG569816}
on this page https://adlp-corp.com/css/styles.css

Now onto the next link https://adlp-corp.com/font/
Ended up in another Tree, first link I click on I get the following file downloaded: fontello.eot I have no idea what the .eot extension is, wasn't really able to get anything out of this file, meh.

Well, that was a waste of time, no flags in second link. 
 
Third link https://adlp-corp.com/images/
Another waste of time.

Last link https://adlp-corp.com/js/
I couldn't find anything new...

Still gotta look for that hidden pdf.

I'm tired not in the mood to continue, 3 flags is good soooo.

I'll come back for the hidden Pdf 

## THe flags 

ADLP{ROBOTS_TXT_G569816} - https://adlp-corp.com/robots.txt
ADLP{SITM4PAS_XML_G569816} - https://adlp-corp.com/sitemap.xml
ADLP{CSS_HSBUSGYIG569816} - https://adlp-corp.com/css/styles.css
