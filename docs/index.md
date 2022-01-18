![OpenIPC Logo](https://cdn.themactep.com/images/logo_openipc.png)

# microbe-web

Microbe Web UI is a default web interface for [OpenIPC firmware][openipcfw].

Microbe Web is lightweight but powerful interface written mostly in shell
and [haserl][haserl]. Web UI listens on port 85.

### UI Translation

To add a missing language translation, please take a look at files in `/files/www/cgi-bin/locale/` directory.
Use `en.sh` file as a template. It contains all the variables you need to assign proper values to.

Make a copy of the file, give it a name according to [ISO 639-1 Code][iso639].

Language file is a shell script that starts with a shebang followed by the name of the language in a comment:
```
#!/bin/sh
# name:Klingonese
```
then below goes a list of variables and their values that constitute the new language support.
Change the values, test the new locale, then submit a patch or create a pull request.


More documentation is available [in our wiki][wiki].

[openipcfw]: https://github.com/OpenIPC/firmware
[haserl]: http://haserl.sourceforge.net/
[iso639]: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
[wiki]: https://github.com/OpenIPC/firmware/wiki/microbe-web

-----

### Support

OpenIPC offers two levels of support.

- Free support through the community (via [chat](https://openipc.org/#telegram-chat-groups) and [mailing lists](https://github.com/OpenIPC/firmware/discussions)).
- Paid commercial support (from the team of developers).

Please consider subscribing for paid commercial support if you intend to use our product for business.
As a paid customer, you will get technical support and maintenance services directly from our skilled team.
Your bug reports and feature requests will get prioritized attention and expedited solutions. It's a win-win
strategy for both parties, that would contribute to the stability your business, and help core developers
to work on the project full-time.

If you have any specific questions concerning our project, feel free to [contact us](mailto:flyrouter@gmail.com).

### Participating and Contribution

If you like what we do, and willing to intensify the development, please consider participating.

You can improve existing code and send us patches. You can add new features missing from our code.

You can help us to write a better documentation, proofread and correct our websites.

You can just donate some money to cover the cost of development and long-term maintaining of what we believe
is going to be the most stable, flexible, and open IP Network Camera Framework for users like yourself.

You can make a financial contribution to the project
at [Open Collective](https://opencollective.com/openipc/contribute/backer-14335/checkout),
or via [PayPal](https://www.paypal.com/donate/?hosted_button_id=C6F7UJLA58MBS),
or via [YooMoney](https://openipc.org/donation/yoomoney.html).

Thank you.

<a href="https://opencollective.com/openipc/contribute/backer-14335/checkout" target="_blank"><img src="https://opencollective.com/webpack/donate/button@2x.png?color=blue" width="375" alt="Open Collective donate button"></a>
<a href="https://www.paypal.com/donate/?hosted_button_id=C6F7UJLA58MBS"><img src="https://www.paypalobjects.com/en_US/IT/i/btn/btn_donateCC_LG.gif" alt="PayPal donate button"></a>
<a href="https://openipc.org/donation/yoomoney.html"><img src="https://yoomoney.ru/transfer/balance-informer/balance?id=596194605&key=291C29A811B500D7" width="140" alt="YooMoney donate button"></a>
