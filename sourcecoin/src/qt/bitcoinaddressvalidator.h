// Copyright (c) 2011-2014 The CM_UppercaseCoinName developers
// Distributed under the MIT/X11 software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef CM_AllCapsCoinNameADDRESSVALIDATOR_H
#define CM_AllCapsCoinNameADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class CM_UppercaseCoinNameAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit CM_UppercaseCoinNameAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

/** CM_UppercaseCoinName address widget validator, checks for a valid CM_LowercaseCoinName address.
 */
class CM_UppercaseCoinNameAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit CM_UppercaseCoinNameAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const;
};

#endif // CM_AllCapsCoinNameADDRESSVALIDATOR_H
